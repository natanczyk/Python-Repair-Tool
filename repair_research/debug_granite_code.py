"""
One-shot diagnostic: prints GraniteCodeLLM's RAW response (before _extract_code
strips/parses it) for a single known-failing submission, so we can see directly
whether it wraps code in ```python fences, leaks prose into the output, or
produces something else entirely.

Run on a GPU node (needs the model loaded):
  python repair_research/debug_granite_code.py [--submission Data/question_1/code/wrong/wrong_1_001.py]
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

_here = Path(__file__).parent.parent
if str(_here) not in sys.path:
    sys.path.insert(0, str(_here))

from Localization.program import Program  # noqa: E402
from repair_research.prompts import build_repair_prompt  # noqa: E402
from repair_research.repair_agent import _extract_code  # noqa: E402
from repair_research.test_runner import run_tests  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--submission", default="Data/question_1/code/wrong/wrong_1_001.py"
    )
    parser.add_argument(
        "--test-suite", default="Data/question_1/test_suite.py"
    )
    parser.add_argument(
        "--description", default="Data/question_1/description.txt"
    )
    args = parser.parse_args()

    submission = Path(args.submission)
    program = Program(
        submission_path=submission,
        test_suite_path=Path(args.test_suite),
        description_path=Path(args.description) if Path(args.description).exists() else None,
    )

    print(f"Submission: {submission}")
    print("Running tests to build the failing-tests hint (iteration 0, repair_none-style) ...")
    result = run_tests(program.get_submission_path(), program.get_test_suite_path())
    if result["has_syntax_error"]:
        failing_hint = result["syntax_error_msg"]
    elif result["solved"]:
        print("This submission already passes all tests — pick a genuinely failing one.")
        return
    else:
        failing_hint = result["failing_tests"]

    prompt = build_repair_prompt(
        program.get_description(),
        program.get_student_code(),
        failing_hint,
        None,  # repair_none uses no suspicious_lines
    )

    print("\n" + "=" * 70)
    print("PROMPT SENT TO MODEL")
    print("=" * 70)
    print(prompt)

    print("\nLoading GraniteCodeLLM ...")
    from LLMs.llm_granite_code import GraniteCodeLLM
    llm = GraniteCodeLLM()
    print("Loaded. Generating (greedy, max_new_tokens as configured) ...\n")

    raw_response = llm.generate_chat([{"role": "user", "content": prompt}])

    print("=" * 70)
    print("RAW RESPONSE (before _extract_code)")
    print("=" * 70)
    print(repr(raw_response))
    print()
    print(raw_response)

    extracted = _extract_code(raw_response)
    print("\n" + "=" * 70)
    print("EXTRACTED CODE (what _extract_code produced, and what gets written to disk)")
    print("=" * 70)
    print(extracted)

    print("\n" + "=" * 70)
    print("DIAGNOSIS")
    print("=" * 70)
    fenced = "```" in raw_response
    print(f"Response contains a ``` fence: {fenced}")
    try:
        ast.parse(extracted)
        print("Extracted code parses as valid Python: YES")
    except SyntaxError as e:
        print(f"Extracted code parses as valid Python: NO -> SyntaxError: {e}")

    if len(raw_response) >= 0 and llm.max_new_tokens:
        # crude truncation signal: response fills (most of) the token budget
        approx_tokens = len(llm.tokenizer.encode(raw_response))
        print(f"Approx. response length: {approx_tokens} tokens (max_new_tokens={llm.max_new_tokens})")
        if approx_tokens >= llm.max_new_tokens - 5:
            print("  -> Response likely got truncated before finishing (near the token budget).")


if __name__ == "__main__":
    main()