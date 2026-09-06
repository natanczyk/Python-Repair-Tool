"""
One-shot diagnostic: prints QwenLLM's RAW response (before _parse_line_numbers
strips/parses it) for a single Bench submission in minimal_notests mode, since
qwen's Bench predictions are ~100% empty across all 3 modes while working fine
on Refactory -- this shows directly whether it's an exception, an unparseable
response, or genuine empty/refusal text.

Run on a GPU node (needs the model loaded):
  python debug_qwen_bench.py [--submission Data_Bench/question_easy/code/wrong/wrong_easy_001.py]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_here = Path(__file__).parent
if str(_here) not in sys.path:
    sys.path.insert(0, str(_here))

_spec_path = _here / "Faulty_Lines_and_Repair_research" / "faulty_lines_finder_bench.py"
import importlib.util
_spec = importlib.util.spec_from_file_location("faulty_lines_finder_bench", _spec_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
_build_llm_prompt = _mod._build_llm_prompt
_parse_line_numbers = _mod._parse_line_numbers


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--submission", default="Data_Bench/question_easy/code/wrong/wrong_easy_001.py"
    )
    parser.add_argument("--descriptions-root", default="Data_Bench/Descriptions")
    args = parser.parse_args()

    submission = Path(args.submission)
    student_code = submission.read_text(encoding="utf-8")
    total_lines = len(student_code.splitlines())

    desc_file = Path(args.descriptions_root) / f"{submission.stem}_description.txt"
    description = desc_file.read_text(encoding="utf-8") if desc_file.exists() else None

    print(f"Submission: {submission}  ({total_lines} lines)")
    print(f"Description file: {desc_file}  (exists: {desc_file.exists()})")

    prompt = _build_llm_prompt(student_code, "minimal_notests", None, description)

    print("\n" + "=" * 70)
    print("PROMPT SENT TO MODEL")
    print("=" * 70)
    print(prompt)

    print("\nLoading QwenLLM ...")
    from LLMs.llm import QwenLLM
    llm = QwenLLM()
    print("Loaded. Generating ...\n")

    raw_response = llm.generate(prompt)

    print("=" * 70)
    print("RAW RESPONSE (before _parse_line_numbers)")
    print("=" * 70)
    print(repr(raw_response))
    print()
    print(raw_response)

    parsed = _parse_line_numbers(raw_response, total_lines)
    print("\n" + "=" * 70)
    print("PARSED LINE NUMBERS")
    print("=" * 70)
    print(parsed)

    if not raw_response.strip():
        print("\nDIAGNOSIS: model returned an empty/whitespace-only response.")
    elif not parsed:
        print("\nDIAGNOSIS: model returned text, but no integers in [1, "
              f"{total_lines}] were found in it -- likely wrong format, "
              "refusal, or line numbers outside the valid range.")
    else:
        print("\nDIAGNOSIS: parsing worked here -- try another submission "
              "if the real run is still showing 100% empty.")


if __name__ == "__main__":
    main()
