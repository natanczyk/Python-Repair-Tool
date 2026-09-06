from __future__ import annotations
import ast
import re
import shutil
import subprocess
import sys
from typing import Any

from Localization.program import Program


class FauxPyRunner:
    def __init__(self, program: Program, timeout: int = 30) -> None:
        self.test_suites = program.get_test_suite_path()
        self.submission = program.get_submission_path()
        self.timeout = timeout

    def _check_syntax(self) -> str | None:
        """Returns a syntax error message if the submission cannot be parsed, else None."""
        source = self.submission.read_text(encoding="utf-8")
        if not source.strip():
            return "SyntaxError: empty submission"
        try:
            
            ast.parse(source)
            return None
        except SyntaxError as e:
            return f"SyntaxError at line {e.lineno}: {e.msg}"

    def _generate_conftest(self) -> None:
        module_name = self.submission.stem
        conftest = (
            "import builtins\n"
            "import importlib\n"
            "import sys\n\n"
            "def pytest_configure(config):\n"
            f"    sys.path.insert(0, r\"{self.submission.parent}\")\n"
            f"    mod = importlib.import_module({module_name!r})\n"
            "    for name in dir(mod):\n"
            "        if not name.startswith('_'):\n"
            "            setattr(builtins, name, getattr(mod, name))\n"
        )
        (self.test_suites.parent / "conftest.py").write_text(conftest, encoding="utf-8")

    def run_fauxpy(self) -> str:
        self._generate_conftest()
        cmd = [
            sys.executable,
            "-m",
            "pytest",
            str(self.test_suites),
            "--src", self.submission.name,
            "--family", "sbfl",
            "--granularity", "statement",
            "-s",
        ]

        timed_out = False
        subprocess_error = False
        output = ""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=str(self.submission.parent),
                timeout=self.timeout,
            )
            output = (result.stdout or "") + "\n" + (result.stderr or "")
            # 0=all passed, 1=some failed, 5=no tests collected are normal
            # negative=killed (OOM), 2/3/4=pytest internal error
            if result.returncode not in (0, 1, 5):
                subprocess_error = True
                print(
                    f"  [fauxpy] subprocess exit {result.returncode} "
                    f"for {self.submission.name} — treating as error\n"
                    f"  stderr: {(result.stderr or '').strip()[:300]}"
                )
        except subprocess.TimeoutExpired:
            timed_out = True
        finally:
            for report_dir in self.submission.parent.glob("FauxPyReport_*"):
                shutil.rmtree(report_dir, ignore_errors=True)

        if timed_out:
            return "TimeoutExpired"
        if subprocess_error:
            return "SubprocessError"
        return output

    def _parse_test_assertions(self) -> dict[str, str]:
        
        """Parses the test file and returns {test_func_name: assertion_expression} mapping.

        The assertion expression is the full assert condition as source, e.g.
        'lab13ex1(468) == 0', giving input + expected output in one string.
        """
        
        if self.test_suites is None:
            return {}
        try:
            source = self.test_suites.read_text(encoding="utf-8")
            tree = ast.parse(source)
        except (OSError, SyntaxError):
            return {}

        assertions: dict[str, str] = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
                for stmt in node.body:
                    if isinstance(stmt, ast.Assert):
                        assertions[node.name] = ast.unparse(stmt.test)
                        break
        return assertions

    def parse_suspiciousness(self, output: str) -> list[dict[str, Any]]:
        suspicious: list[dict[str, Any]] = []
        capture = False

        for raw_line in output.splitlines():
            line = raw_line.strip()

            if "Scores for Ochiai" in line:
                capture = True
                continue

            if not capture:
                continue

            # skip separator lines and section headers
            if not line or line.startswith("=") or line.startswith("-"):
                if suspicious:
                    break
                continue

            parts = [part.strip() for part in line.split("|") if part.strip()]
            if len(parts) < 3:
                continue

            try:
                suspicious.append(
                    {
                        "file": parts[0],
                        "line": int(parts[1]),
                        "score": float(parts[2]),
                    }
                )
            except ValueError:
                continue

        suspicious.sort(key=lambda item: item["score"], reverse=True)
        return suspicious

    def format_suspicious_lines(self, suspicious: list[dict[str, Any]]) -> str | None:
        if not suspicious:
            return None
        return "\n".join(
            f"Line {item['line']}: suspiciousness {item['score']:.4f}"
            for item in suspicious
        )

    def format_incorrect_tests(self, output: str) -> str | None:
        """Extracts failing tests and, for each, reconstructs the full assertion
        (including inputs and expected value) by parsing the test file."""
        lines = output.splitlines()
        failed = [line for line in lines if line.strip().startswith("FAILED")]

        if not failed:
            return None

        assertions = self._parse_test_assertions()
        formatted = []

        for line in failed:
            # pytest FAILED lines look like: FAILED path/file.py::test_caseN - ...
            name_match = re.search(r"::(\w+)", line)
            test_name = name_match.group(1) if name_match else None
            assertion = assertions.get(test_name) if test_name else None

            if assertion:
                # e.g. "test_case2: lab13ex1(12426374856) == 1375"
                formatted.append(f"{test_name}: {assertion}")
            else:
                formatted.append(line.strip())

        return "\n".join(formatted)

    def get_analysis(self) -> dict[str, Any]:
        syntax_error = self._check_syntax()
        if syntax_error:
            return {
                "output": syntax_error,
                "suspicious": [],
                "suspicious_text": None,
                "failing_tests": None,
                "has_syntax_error": True,
                "timed_out": False,
            }

        output = self.run_fauxpy()

        if output == "TimeoutExpired":
            return {
                "output": output,
                "suspicious": [],
                "suspicious_text": None,
                "failing_tests": "TimeoutExpired",
                "has_syntax_error": False,
                "timed_out": True,
            }

        if output == "SubprocessError":
            return {
                "output": output,
                "suspicious": [],
                "suspicious_text": None,
                "failing_tests": "SubprocessError",
                "has_syntax_error": False,
                "timed_out": True,  # reuse timed_out flag → repair loops break without marking solved
            }

        suspicious = self.parse_suspiciousness(output)

        return {
            "output": output,
            "suspicious": suspicious,
            "suspicious_text": self.format_suspicious_lines(suspicious),
            "failing_tests": self.format_incorrect_tests(output),
            "has_syntax_error": False,
            "timed_out": False,
        }
