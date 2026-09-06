"""
Fault localization for a single arbitrary submission, independent of the
question_N/ directory layout used by faulty_lines_finder.py.

--mode choices:
    fauxpy          SBFL via FauxPy — needs --test-suite (a pytest file).
    ranking         LLM ranks ALL lines by suspiciousness using test I/O pairs.
    minimal_tests   LLM identifies minimal buggy lines using test I/O pairs.
    minimal_notests LLM identifies minimal buggy lines using description only (no tests).

Requirements on your files:
  - --submission: the buggy .py file to localize.
  - --test-suite: required for --mode fauxpy only — a pytest file whose test
    functions are named test_*, each containing a single
    `assert some_call(...) == expected` statement (parsed to build the
    failing-test summary; more complex test bodies won't be reported
    correctly).
  - --test-pairs-dir: required for --mode ranking / minimal_tests — a
    directory containing matched input_*.txt / output_*.txt files, one pair
    per test case (e.g. input_001.txt + output_001.txt), shown to the model
    as raw text. This is independent of --test-suite -- fauxpy runs pytest,
    the other modes never execute the code at all.
  - --description: plain-text assignment description. Required for
    --mode minimal_notests; optional extra context for the other modes.

Output: a single JSONL line written to --output-file:
    {"program_name": "<submission name>", "buggy_lines": [3, 7, ...]}

Usage:
  python Faulty_Lines_and_Repair_research/faulty_lines_finder_FOR_YOU.py \\
    --mode fauxpy \\
    --submission path/to/buggy_submission.py \\
    --test-suite path/to/test_suite.py \\
    --output-file path/to/result.jsonl

  python Faulty_Lines_and_Repair_research/faulty_lines_finder_FOR_YOU.py \\
    --mode minimal_tests --model qwen \\
    --submission path/to/buggy_submission.py \\
    --test-pairs-dir path/to/test_io \\
    --output-file path/to/result.jsonl
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Protocol, runtime_checkable

_here = Path(__file__).parent.parent
if str(_here) not in sys.path:
    sys.path.insert(0, str(_here))


@runtime_checkable
class LLM(Protocol):
    def generate(self, prompt: str) -> str: ...


def _number_code(code: str) -> str:
    return "\n".join(f"{i+1:3}: {line}" for i, line in enumerate(code.splitlines()))


def _load_test_pairs(test_pairs_dir: Path) -> list[tuple[str, str]]:
    pairs = []
    for inp_path in sorted(test_pairs_dir.glob("input_*.txt")):
        out_path = test_pairs_dir / f"output_{inp_path.name[len('input_'):]}"
        if out_path.exists():
            pairs.append((
                inp_path.read_text(encoding="utf-8").strip(),
                out_path.read_text(encoding="utf-8").strip(),
            ))
    return pairs


def _parse_line_numbers(text: str, total_lines: int) -> list[int]:
    seen: list[int] = []
    for m in re.finditer(r'\b(\d+)\b', text):
        n = int(m.group(1))
        if 1 <= n <= total_lines and n not in seen:
            seen.append(n)
    return seen


def _build_llm_prompt(
    student_code: str,
    mode: str,
    test_pairs: list[tuple[str, str]] | None = None,
    description: str | None = None,
) -> str:
    desc_section = f"\nAssignment:\n{description}\n" if description else ""
    total_lines = len(student_code.splitlines())
    numbered = _number_code(student_code)

    if mode == "ranking":
        tests_section = "\n".join(
            f"  Call: {inp}\n  Expected: {out}" for inp, out in (test_pairs or [])
        )
        return f"""You are a fault localization expert. Given a buggy Python program and its failing test cases, rank ALL {total_lines} lines from most likely to contain the bug to least likely.

Reply with ONLY all line numbers separated by commas, ordered from most to least suspicious (e.g. "3, 7, 1, 5, 2, ..."). Include every line number from 1 to {total_lines}. Nothing else.
{desc_section}
Test cases:
{tests_section}

Buggy code:
{numbered}

All line numbers ranked from most to least suspicious:""".strip()

    if mode == "minimal_tests":
        test_section = "\n".join(
            f"Input: {inp}\nExpected Output: {out}"
            for inp, out in (test_pairs or [])
        )
        return f"""You are a fault localization expert. Given a buggy Python program, its assignment description, and its failing test cases, identify the minimal set of line numbers that need to be changed for the code to become correct.

Reply with ONLY the line numbers separated by commas (e.g. "3, 7"). Include only lines that contain an actual bug — no more than necessary. Nothing else.
{desc_section}
{test_section}


Buggy code:
{numbered}

Minimal set of buggy line numbers (comma-separated):""".strip()

    # minimal_notests — description + code only, no test pairs
    return f"""You are a fault localization expert. Given only the assignment description and a buggy Python program, identify the minimal set of line numbers that need to be changed for the code to become correct.

Reply with ONLY the line numbers separated by commas (e.g. "3, 7"). Include only lines that contain an actual bug — no more than necessary. Nothing else.
{desc_section}
Buggy code:
{numbered}

Minimal set of buggy line numbers (comma-separated):""".strip()


def run_fauxpy(
    submission: Path,
    test_suite: Path,
    description: Path | None,
    timeout: int = 30,
) -> list[int]:
    from Localization.fauxpy_runner import FauxPyRunner
    from Localization.program import Program

    program = Program(
        submission_path=submission,
        test_suite_path=test_suite,
        description_path=description,
    )
    analysis = FauxPyRunner(program, timeout=timeout).get_analysis()
    return [e["line"] for e in analysis["suspicious"]]


def run_llm(
    submission: Path,
    mode: str,
    llm: LLM,
    test_pairs_dir: Path | None,
    description: Path | None,
) -> list[int]:
    student_code = submission.read_text(encoding="utf-8")
    total_lines = len(student_code.splitlines())
    test_pairs = _load_test_pairs(test_pairs_dir) if test_pairs_dir else []
    desc_text = description.read_text(encoding="utf-8") if description else None

    prompt = _build_llm_prompt(student_code, mode, test_pairs, desc_text)
    response = llm.generate(prompt)
    return _parse_line_numbers(response, total_lines)


def _load_llm(model_key: str) -> LLM:
    if model_key == "qwen":
        from LLMs.llm import QwenLLM
        return QwenLLM()
    if model_key == "qwen3_27b":
        from LLMs.llm_qwen3_27b import Qwen3_27B_LLM
        return Qwen3_27B_LLM()
    if model_key == "qwen3_coder":
        from LLMs.llm_qwen3_coder import Qwen3CoderLLM
        return Qwen3CoderLLM()
    if model_key == "gemma4":
        from LLMs.llm_gemma4 import Gemma4LLM
        return Gemma4LLM()
    if model_key == "granite4":
        from LLMs.llm_granite4 import Granite4LLM
        return Granite4LLM()
    if model_key == "codegemma":
        from LLMs.llm_codegemma import CodeGemmaLLM
        return CodeGemmaLLM()
    if model_key == "granite_code":
        from LLMs.llm_granite_code import GraniteCodeLLM
        return GraniteCodeLLM()
    if model_key == "codellama":
        from LLMs.llm_codellama import CodeLlamaLLM
        return CodeLlamaLLM()
    raise ValueError(f"Unknown model: {model_key!r}")


_ALL_MODELS = [
    "qwen", "qwen3_27b", "qwen3_coder",
    "gemma4", "codegemma",
    "granite4", "granite_code",
    "codellama",
]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fault localization on a single arbitrary submission."
    )
    parser.add_argument(
        "--mode", required=True,
        choices=["fauxpy", "ranking", "minimal_tests", "minimal_notests"],
    )
    parser.add_argument("--submission", required=True, help="Path to the buggy .py file.")
    parser.add_argument(
        "--test-suite", default=None,
        help="Path to a pytest test suite file. Required for --mode fauxpy.",
    )
    parser.add_argument(
        "--test-pairs-dir", default=None,
        help=(
            "Directory with matched input_*.txt / output_*.txt files. "
            "Required for --mode ranking and --mode minimal_tests."
        ),
    )
    parser.add_argument(
        "--description", default=None,
        help="Path to a plain-text assignment description. Required for --mode minimal_notests.",
    )
    parser.add_argument(
        "--model", choices=_ALL_MODELS,
        help="LLM model to use. Required for ranking/minimal_tests/minimal_notests.",
    )
    parser.add_argument(
        "--output-file", required=True,
        help="Path to write the single-line JSONL result to.",
    )
    parser.add_argument("--fauxpy-timeout", type=int, default=30)
    args = parser.parse_args()

    submission = Path(args.submission)
    if not submission.exists():
        sys.exit(f"Submission not found: {submission}")

    description = Path(args.description) if args.description else None
    if description is not None and not description.exists():
        sys.exit(f"Description not found: {description}")

    if args.mode == "fauxpy":
        if not args.test_suite:
            sys.exit("--test-suite is required for --mode fauxpy")
        test_suite = Path(args.test_suite)
        if not test_suite.exists():
            sys.exit(f"Test suite not found: {test_suite}")
        buggy_lines = run_fauxpy(submission, test_suite, description, timeout=args.fauxpy_timeout)
    else:
        if args.mode == "minimal_notests" and description is None:
            sys.exit("--description is required for --mode minimal_notests")
        if args.mode in ("ranking", "minimal_tests") and not args.test_pairs_dir:
            sys.exit(f"--test-pairs-dir is required for --mode {args.mode}")

        test_pairs_dir = Path(args.test_pairs_dir) if args.test_pairs_dir else None
        if test_pairs_dir is not None and not test_pairs_dir.exists():
            sys.exit(f"Test pairs directory not found: {test_pairs_dir}")

        if not args.model:
            sys.exit("--model is required for LLM-based modes.")
        print(f"Loading model '{args.model}' …")
        llm = _load_llm(args.model)
        print("Model loaded.\n")

        buggy_lines = run_llm(submission, args.mode, llm, test_pairs_dir, description)

    record = {"program_name": submission.name, "buggy_lines": buggy_lines}
    output_file = Path(args.output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(record) + "\n", encoding="utf-8")

    print(f"buggy_lines: {buggy_lines}")
    print(f"Result written to: {output_file}")


if __name__ == "__main__":
    main()