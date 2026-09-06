"""Lightweight test runner (no FauxPy) for checking whether a submission passes."""
from __future__ import annotations

import ast
import re
import subprocess
import sys
from pathlib import Path


def _check_syntax(submission: Path) -> str | None:
    source = submission.read_text(encoding="utf-8")
    if not source.strip():
        return "SyntaxError: empty submission"
    try:
        ast.parse(source)
        return None
    except SyntaxError as e:
        return f"SyntaxError at line {e.lineno}: {e.msg}"


def _generate_conftest(submission: Path, test_suite: Path) -> None:
    module_name = submission.stem
    conftest = (
        "import builtins\n"
        "import importlib\n"
        "import sys\n\n"
        "def pytest_configure(config):\n"
        f"    sys.path.insert(0, r\"{submission.parent}\")\n"
        f"    mod = importlib.import_module({module_name!r})\n"
        "    for name in dir(mod):\n"
        "        if not name.startswith('_'):\n"
        "            setattr(builtins, name, getattr(mod, name))\n"
    )
    (test_suite.parent / "conftest.py").write_text(conftest, encoding="utf-8")


def _parse_test_assertions(test_suite: Path) -> dict[str, str]:
    try:
        source = test_suite.read_text(encoding="utf-8")
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


def _format_failing(output: str, test_suite: Path) -> str | None:
    lines = output.splitlines()
    failed = [ln for ln in lines if ln.strip().startswith("FAILED")]
    if not failed:
        return None
    assertions = _parse_test_assertions(test_suite)
    formatted = []
    for line in failed:
        m = re.search(r"::(\w+)", line)
        name = m.group(1) if m else None
        assertion = assertions.get(name) if name else None
        formatted.append(f"{name}: {assertion}" if assertion else line.strip())
    return "\n".join(formatted)


def run_tests(submission: Path, test_suite: Path, timeout: int = 20) -> dict:
    """
    Run pytest on submission without FauxPy instrumentation.

    Returns:
        solved          (bool)  — True if all tests pass
        failing_tests   (str|None) — formatted failing test lines, or None if all pass
        has_syntax_error (bool)
        syntax_error_msg (str|None)
        timed_out       (bool)
    """
    syntax_err = _check_syntax(submission)
    if syntax_err:
        return {
            "solved": False,
            "failing_tests": None,
            "has_syntax_error": True,
            "syntax_error_msg": syntax_err,
            "timed_out": False,
        }

    _generate_conftest(submission, test_suite)
    cmd = [sys.executable, "-m", "pytest", str(test_suite), "-s"]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(test_suite.parent),
            timeout=timeout,
        )
        output = (result.stdout or "") + "\n" + (result.stderr or "")
        if result.returncode not in (0, 1, 5):
            return {
                "solved": False,
                "failing_tests": f"TestRunnerError (exit {result.returncode})",
                "has_syntax_error": False,
                "syntax_error_msg": None,
                "timed_out": True,
            }
        failing = _format_failing(output, test_suite)
        return {
            "solved": failing is None,
            "failing_tests": failing,
            "has_syntax_error": False,
            "syntax_error_msg": None,
            "timed_out": False,
        }
    except subprocess.TimeoutExpired:
        return {
            "solved": False,
            "failing_tests": "TimeoutExpired",
            "has_syntax_error": False,
            "syntax_error_msg": None,
            "timed_out": True,
        }
