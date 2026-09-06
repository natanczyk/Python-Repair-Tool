"""
Run a single repair-loop experiment on an arbitrary submission, independent of
the Refactory/QuixBugs/Bench question_N/ directory layout used by run_repair.py.

Four repair types:
  none      — no localization; code + failing tests only
  fauxpy    — FauxPy Ochiai scores provided at each iteration
  best_loc  — Gemma4 localizes live at each iteration; repair model fixes
  self_llm  — same model first localizes, then repairs, at each iteration

Requirements on your files:
  - --test-suite must be a pytest file whose test functions are named test_*,
    each containing a single `assert some_call(...) == expected` statement
    (the repair prompts and the failing-test summaries are built by parsing
    this assert statement, so more complex test bodies won't be reported
    correctly).
  - --submission's public function/class names must match whatever the test
    suite calls directly (no imports are added other than the submission
    itself) — at runtime a conftest.py is generated next to the test suite
    that imports the submission module and injects its public names into
    the test file's namespace. That conftest.py is written to (and
    overwritten in) the test suite's own directory as a side effect of
    running this script.
  - --description is optional; it's only extra context for the model and
    has no effect on how the code is executed or checked.

Output (written to --output-dir):
  result.json                    {"submission": ..., "solved": true/false,
                                   "iterations": N, "repair_type": ...,
                                   "repair_model": ..., "repaired_file": ...}
  repaired_<submission-name>.py  only written if solved

Usage:
  python repair_research/run_repair_FOR_YOU.py \\
    --repair-type fauxpy \\
    --repair-model qwen \\
    --submission path/to/buggy_submission.py \\
    --test-suite path/to/test_suite.py \\
    --description path/to/description.txt \\
    --output-dir path/to/output

  # best_loc and self_llm ignore --description for localization; best_loc
  # additionally loads Gemma4 (unless --repair-model is already gemma4).
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

_here = Path(__file__).parent.parent
if str(_here) not in sys.path:
    sys.path.insert(0, str(_here))

from Localization.program import Program  # noqa: E402
from repair_research.repair_agent import RepairAgent  # noqa: E402

_MODEL_CHOICES = [
    "qwen", "qwen3_27b", "qwen3_coder",
    "gemma4", "granite4",
    "codegemma", "granite_code", "codellama",
]

_REPAIR_TYPES = ["none", "fauxpy", "best_loc", "self_llm"]


def _build_llm(model_key: str):
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


def run_one(
    repair_type: str,
    repair_model: str,
    submission: Path,
    test_suite: Path,
    description: Path | None,
    llm,
    output_dir: Path,
    loc_llm=None,
    max_attempts: int = 4,
) -> dict:
    program = Program(
        submission_path=submission,
        test_suite_path=test_suite,
        description_path=description,
    )

    with tempfile.TemporaryDirectory(prefix="repair_work_") as tmp:
        work_dir = Path(tmp)
        agent = RepairAgent(
            program=program,
            llm=llm,
            work_dir=work_dir,
            max_attempts=max_attempts,
        )

        if repair_type == "none":
            agent.repair_none()
        elif repair_type == "fauxpy":
            agent.repair_fauxpy()
        elif repair_type == "best_loc":
            agent.repair_best_loc(loc_llm)
        elif repair_type == "self_llm":
            agent.repair_self_llm()

    output_dir.mkdir(parents=True, exist_ok=True)

    repaired_file: str | None = None
    if agent.solved and agent.final_code:
        repaired_path = output_dir / f"repaired_{submission.name}"
        repaired_path.write_text(agent.final_code, encoding="utf-8")
        repaired_file = str(repaired_path)

    record = {
        "submission": submission.name,
        "solved": agent.solved,
        "iterations": agent.iterations,
        "repair_type": repair_type,
        "repair_model": repair_model,
        "repaired_file": repaired_file,
    }
    (output_dir / "result.json").write_text(
        json.dumps(record, indent=2), encoding="utf-8"
    )
    return record


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run a single repair-loop experiment on an arbitrary submission."
    )
    parser.add_argument("--repair-type", required=True, choices=_REPAIR_TYPES)
    parser.add_argument("--repair-model", required=True, choices=_MODEL_CHOICES)
    parser.add_argument("--submission", required=True, help="Path to the buggy .py file.")
    parser.add_argument("--test-suite", required=True, help="Path to the pytest test suite file.")
    parser.add_argument(
        "--description", default=None,
        help="Optional path to a plain-text assignment description.",
    )
    parser.add_argument(
        "--output-dir", required=True,
        help="Where to write result.json and the repaired code (if solved).",
    )
    parser.add_argument("--max-attempts", type=int, default=4)
    args = parser.parse_args()

    submission = Path(args.submission)
    test_suite = Path(args.test_suite)
    description = Path(args.description) if args.description else None
    output_dir = Path(args.output_dir)

    if not submission.exists():
        sys.exit(f"Submission not found: {submission}")
    if not test_suite.exists():
        sys.exit(f"Test suite not found: {test_suite}")
    if description is not None and not description.exists():
        sys.exit(f"Description not found: {description}")

    print(f"Loading model '{args.repair_model}' …")
    llm = _build_llm(args.repair_model)
    print("Model loaded.\n")

    # Load Gemma4 as the localization model for best_loc
    loc_llm = None
    if args.repair_type == "best_loc":
        if args.repair_model == "gemma4":
            print("Repair model is Gemma4 — reusing it for localization.\n")
            loc_llm = llm
        else:
            print("Loading Gemma4 as localization model …")
            from LLMs.llm_gemma4 import Gemma4LLM
            loc_llm = Gemma4LLM()
            print("Gemma4 loaded.\n")

    print(f"{'='*55}")
    print(f"  REPAIR TYPE  : {args.repair_type}")
    print(f"  REPAIR MODEL : {args.repair_model}")
    print(f"  SUBMISSION   : {submission}")
    print(f"  TEST SUITE   : {test_suite}")
    print(f"  MAX ATTEMPTS : {args.max_attempts}")
    print(f"{'='*55}")

    record = run_one(
        repair_type=args.repair_type,
        repair_model=args.repair_model,
        submission=submission,
        test_suite=test_suite,
        description=description,
        llm=llm,
        output_dir=output_dir,
        loc_llm=loc_llm,
        max_attempts=args.max_attempts,
    )

    status = "solved" if record["solved"] else "failed"
    print(f"\n{status} in {record['iterations']} iteration(s).")
    print(f"Result saved to: {output_dir / 'result.json'}")
    if record["repaired_file"]:
        print(f"Repaired code saved to: {record['repaired_file']}")


if __name__ == "__main__":
    main()