"""
Fault localization for student submissions.

All modes output JSONL matching ground_truth format:
    {"program_name": "wrong_1_001.py", "buggy_lines": [3]}

Results are saved next to ground_truth.jsonl in each question folder:
    Data/question_N/fauxpy_localization.jsonl                        (fauxpy)
    Data/question_N/llm_<model>_localization.jsonl                   (ranking)
    Data/question_N/llm_<model>_minimal_localization.jsonl           (minimal_tests)
    Data/question_N/llm_<model>_minimal_notests_localization.jsonl   (minimal_notests)

--mode choices:
    fauxpy          SBFL via FauxPy — needs a pytest test suite file per question.
    ranking         LLM ranks ALL lines by suspiciousness using test I/O pairs.
    minimal_tests   LLM identifies minimal buggy lines using test I/O pairs.
    minimal_notests LLM identifies minimal buggy lines using description only (no tests).

Example usage (server):
    python faulty_lines_finder.py --mode ranking --model qwen3_27b \\
        --questions-root /data/Data --questions 1 2 3 4 5

    python faulty_lines_finder.py --mode minimal_notests --model gemma4 \\
        --questions-root /data/Data --questions 1 2 3 4 5

    python faulty_lines_finder.py --mode fauxpy \\
        --questions-root /data/Data --questions 1 2 3 4 5 \\
        --test-suite-pattern /data/test_suites/test_question_{n}.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Protocol, runtime_checkable


# ── LLM interface (any object with .generate() qualifies) ─────────────────────

@runtime_checkable
class LLM(Protocol):
    def generate(self, prompt: str) -> str: ...


# ── shared helpers ────────────────────────────────────────────────────────────

def _number_code(code: str) -> str:
    return "\n".join(f"{i+1:3}: {line}" for i, line in enumerate(code.splitlines()))


def _load_test_pairs(ans_dir: Path) -> list[tuple[str, str]]:
    pairs = []
    for inp_path in sorted(ans_dir.glob("input_*.txt")):
        out_path = ans_dir / f"output_{inp_path.name[len('input_'):]}"
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


# ── Method 1: FauxPy SBFL ────────────────────────────────────────────────────

def run_fauxpy_localization(
    wrong_dir: Path,
    test_suite_path: Path | None,
    output_file: Path,
    description_path: Path | None = None,
    test_suites_dir: Path | None = None,
) -> None:
    """SBFL via FauxPy. Requires a pytest-compatible test suite file.

    Two modes:
    - Shared test suite (Refactory): pass test_suite_path; all submissions use it.
    - Per-submission test suites (Data_Bench): pass test_suites_dir; each submission
      uses test_suites_dir/test_{submission_stem}.py.
    """
    from Localization.fauxpy_runner import FauxPyRunner
    from Localization.program import Program

    output_file.parent.mkdir(parents=True, exist_ok=True)
    submissions = sorted(wrong_dir.glob("wrong_*.py"))
    print(f"[fauxpy] {len(submissions)} submissions -> {output_file}")

    with output_file.open("w", encoding="utf-8") as f:
        for i, submission in enumerate(submissions, 1):
            # Resolve test suite path: per-submission dir takes priority
            if test_suites_dir is not None:
                ts_path = test_suites_dir / f"test_{submission.stem}.py"
                if not ts_path.exists():
                    print(f"  [skip] {submission.name}: no test suite ({ts_path.name})")
                    record = {"program_name": submission.name, "buggy_lines": []}
                    f.write(json.dumps(record) + "\n")
                    f.flush()
                    continue
            else:
                ts_path = test_suite_path

            program = Program(
                submission_path=submission,
                test_suite_path=ts_path,
                description_path=description_path,
            )
            try:
                analysis = FauxPyRunner(program).get_analysis()
                buggy_lines = [e["line"] for e in analysis["suspicious"]]
            except Exception as exc:
                print(f"  [error] {submission.name}: {exc}")
                buggy_lines = []

            record = {"program_name": submission.name, "buggy_lines": buggy_lines}
            f.write(json.dumps(record) + "\n")
            f.flush()
            print(f"  [{i}/{len(submissions)}] {submission.name}: {buggy_lines}")


# ── Method 2: LLM-based ───────────────────────────────────────────────────────

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
        return f"""You are a fault localization expert. Given only assignment description and a buggy Python program, identify the minimal set of line numbers that need to be changed for the code to become correct.

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


def run_llm_localization(
    wrong_dir: Path,
    ans_dir: Path | None,
    output_file: Path,
    llm: LLM,
    mode: str,
    description_path: Path | None = None,
    descriptions_root: Path | None = None,
) -> None:
    """LLM-based fault localization (ranking, minimal_tests, or minimal_notests).

    Supports two ans/ layouts:
      Shared   — ans_dir/input_001.txt  (one set of I/O for all submissions, e.g. Data/)
      Per-sub  — ans_dir/<submission_stem>/input_001.txt  (Data_Bench layout)
    """
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Detect shared vs per-submission I/O layout
    shared_pairs: list[tuple[str, str]] | None = None
    if ans_dir is not None and any(ans_dir.glob("input_*.txt")):
        shared_pairs = _load_test_pairs(ans_dir)

    shared_description = description_path.read_text(encoding="utf-8") if description_path else None

    submissions = sorted(wrong_dir.glob("wrong_*.py"))
    print(f"[{mode}] {len(submissions)} submissions -> {output_file}")

    with output_file.open("w", encoding="utf-8") as f:
        for i, submission in enumerate(submissions, 1):
            # Resolve I/O pairs for this submission
            if shared_pairs is not None:
                test_pairs = shared_pairs
            elif ans_dir is not None:
                sub_ans = ans_dir / submission.stem
                test_pairs = _load_test_pairs(sub_ans) if sub_ans.exists() else []
            else:
                test_pairs = []

            # Resolve description for this submission
            if shared_description is not None:
                description = shared_description
            elif descriptions_root is not None:
                desc_file = descriptions_root / f"{submission.stem}_description.txt"
                description = desc_file.read_text(encoding="utf-8") if desc_file.exists() else None
            else:
                description = None

            try:
                student_code = submission.read_text(encoding="utf-8")
                total_lines = len(student_code.splitlines())
                prompt = _build_llm_prompt(student_code, mode, test_pairs, description)
                response = llm.generate(prompt)
                buggy_lines = _parse_line_numbers(response, total_lines)
            except Exception as exc:
                print(f"  [error] {submission.name}: {exc}")
                buggy_lines = []

            record = {"program_name": submission.name, "buggy_lines": buggy_lines}
            f.write(json.dumps(record) + "\n")
            f.flush()
            print(f"  [{i}/{len(submissions)}] {submission.name}: {buggy_lines}")


# ── output file name per mode ─────────────────────────────────────────────────

def _output_filename(mode: str, model_key: str | None) -> str:
    if mode == "fauxpy":
        return "fauxpy_localization.jsonl"
    if mode == "ranking":
        return f"llm_{model_key}_localization.jsonl"
    if mode == "minimal_tests":
        return f"llm_{model_key}_minimal_localization.jsonl"
    return f"llm_{model_key}_minimal_notests_localization.jsonl"


# ── multi-question runner ─────────────────────────────────────────────────────

def run_questions(
    modes: list[str],
    questions_root: Path,
    question_numbers: list,
    model_key: str | None = None,
    llm: LLM | None = None,
    test_suite_pattern: str | None = None,
    test_suites_dir: Path | None = None,
    results_root: Path | None = None,
    descriptions_root: Path | None = None,
) -> None:
    """Loop over modes then question folders. Model is shared across all LLM modes."""
    for mode in modes:
        print(f"\n{'='*50}")
        print(f"  MODE: {mode}" + (f"  |  MODEL: {model_key}" if model_key else ""))
        print(f"{'='*50}")

        for n in question_numbers:
            q_dir = questions_root / f"question_{n}"
            wrong_dir = q_dir / "code" / "wrong"
            ans_dir = q_dir / "ans"
            desc_path = q_dir / "description.txt"
            description_path = desc_path if desc_path.exists() else None

            if not wrong_dir.exists():
                print(f"[skip] question_{n}: wrong dir not found ({wrong_dir})")
                continue

            print(f"\n=== question_{n} ===")
            out_dir = (results_root / f"question_{n}") if results_root else q_dir
            out_dir.mkdir(parents=True, exist_ok=True)
            output_file = out_dir / _output_filename(mode, model_key)

            if mode == "fauxpy":
                if test_suites_dir is not None:
                    # Per-submission test suites (Data_Bench style)
                    run_fauxpy_localization(
                        wrong_dir=wrong_dir,
                        test_suite_path=None,
                        output_file=output_file,
                        description_path=description_path,
                        test_suites_dir=test_suites_dir,
                    )
                else:
                    # Shared test suite per question (Refactory style)
                    if test_suite_pattern:
                        test_suite_path = Path(test_suite_pattern.format(n=n))
                    else:
                        test_suite_path = q_dir / "test_suite.py"
                    if not test_suite_path.exists():
                        print(f"[skip] question_{n}: test suite not found ({test_suite_path})")
                        continue
                    run_fauxpy_localization(
                        wrong_dir=wrong_dir,
                        test_suite_path=test_suite_path,
                        output_file=output_file,
                        description_path=description_path,
                    )
            else:
                needs_tests = mode in ("ranking", "minimal_tests")
                if needs_tests and not ans_dir.exists():
                    print(f"[skip] question_{n}: ans dir not found ({ans_dir})")
                    continue
                run_llm_localization(
                    wrong_dir=wrong_dir,
                    ans_dir=ans_dir if needs_tests else None,
                    output_file=output_file,
                    llm=llm,
                    mode=mode,
                    description_path=description_path,
                    descriptions_root=descriptions_root,
                )


# ── CLI ───────────────────────────────────────────────────────────────────────

def _load_llm(model_key: str) -> LLM:
    """Load only the requested model."""
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


_LLM_MODES = ("ranking", "minimal_tests", "minimal_notests")
_ALL_MODELS = [
    "qwen", "qwen3_27b", "qwen3_coder",
    "gemma4", "codegemma",
    "granite4", "granite_code",
    "codellama",
]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fault localization across question folders. Outputs JSONL next to ground_truth.jsonl."
    )
    parser.add_argument(
        "--mode", required=True, nargs="+",
        choices=["fauxpy", "ranking", "minimal_tests", "minimal_notests", "all_llm"],
        help=(
            "One or more modes to run (model is loaded once and reused). "
            "all_llm: shorthand for ranking + minimal_tests + minimal_notests. "
            "fauxpy: SBFL via FauxPy (needs --test-suite-pattern). "
            "ranking: LLM ranks all lines by suspiciousness using test I/O pairs. "
            "minimal_tests: LLM finds minimal buggy lines using test I/O pairs. "
            "minimal_notests: LLM finds minimal buggy lines using description only."
        ),
    )
    parser.add_argument(
        "--questions-root", required=True,
        help="Base directory containing question_1, question_2, … folders (e.g. Data/).",
    )
    parser.add_argument(
        "--questions", nargs="+", type=str, default=["1", "2", "3", "4", "5"],
        metavar="N",
        help="Question identifiers to process (default: 1 2 3 4 5). "
             "Accepts integers (question_1) or strings (easy → question_easy).",
    )
    parser.add_argument(
        "--descriptions-root", default=None,
        help="Directory containing per-submission description files named "
             "<submission_stem>_description.txt (e.g. Data_Bench/Descriptions/). "
             "Used when each submission has a unique problem description.",
    )
    parser.add_argument(
        "--model", choices=_ALL_MODELS,
        help="LLM model to use (required when any LLM mode is selected).",
    )
    parser.add_argument(
        "--test-suite-pattern",
        help=(
            "Path template for pytest test files, with {n} as the question number. "
            "Used for fauxpy mode (Refactory style: one shared test file per question). "
            "Example: /data/test_suites/test_question_{n}.py"
        ),
    )
    parser.add_argument(
        "--test-suites-dir",
        help=(
            "Directory containing per-submission pytest test files named "
            "test_{submission_stem}.py (Data_Bench style). "
            "Takes priority over --test-suite-pattern when both are given. "
            "Example: Data_Bench/test_suites/"
        ),
    )
    parser.add_argument(
        "--results-root", default=None,
        help=(
            "Directory where JSONL result files are saved. "
            "Results go to <results-root>/question_N/<filename>.jsonl. "
            "Defaults to saving alongside the submissions inside questions-root."
        ),
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()

    # Expand all_llm shorthand and deduplicate while preserving order
    expanded: list[str] = []
    for m in args.mode:
        if m == "all_llm":
            for llm_mode in _LLM_MODES:
                if llm_mode not in expanded:
                    expanded.append(llm_mode)
        elif m not in expanded:
            expanded.append(m)
    modes = expanded

    llm = None
    needs_llm = any(m in _LLM_MODES for m in modes)
    if needs_llm:
        if not args.model:
            print("Error: --model is required when any LLM mode is selected.", file=sys.stderr)
            sys.exit(1)
        print(f"Loading model '{args.model}' …")
        llm = _load_llm(args.model)
        print("Model loaded.")

    run_questions(
        modes=modes,
        questions_root=Path(args.questions_root),
        question_numbers=args.questions,
        model_key=args.model,
        llm=llm,
        test_suite_pattern=args.test_suite_pattern,
        test_suites_dir=Path(args.test_suites_dir) if args.test_suites_dir else None,
        results_root=Path(args.results_root) if args.results_root else None,
        descriptions_root=Path(args.descriptions_root) if args.descriptions_root else None,
    )
