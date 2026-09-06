"""
Pre-compute Gemma4 localization for all Refactory submissions.

Runs once before best_loc repair experiments. Saves a cache file:
  <results_root>/question_N/gemma4_loc_cache.jsonl

Each line:
  {"submission": "wrong_1_001.py", "suspicious_lines": "Line 5: ...\nLine 3: ...", "skipped": false}

  suspicious_lines is null if the original submission already passes, has a syntax error,
  or if the test runner timed out.

Usage:
  python repair_research/precompute_loc.py \\
    --questions-root /home/guests3/nkg/MASTER_PROJECT/Data \\
    --results-root /media/generalstorage4/nkgstorage/Results/repair \\
    [--questions 1 2 3 4 5]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_here = Path(__file__).parent.parent
if str(_here) not in sys.path:
    sys.path.insert(0, str(_here))

from LLMs.llm_gemma4 import Gemma4LLM  # noqa: E402
from Localization.program import Program  # noqa: E402
from repair_research.prompts import build_localization_prompt  # noqa: E402
from repair_research.test_runner import run_tests  # noqa: E402


def precompute_question(
    q_dir: Path,
    llm: Gemma4LLM,
    results_root: Path,
    resume: bool,
) -> None:
    wrong_dir = q_dir / "code" / "wrong"
    test_suite = q_dir / "test_suite.py"
    if not wrong_dir.exists() or not test_suite.exists():
        print(f"  [skip] missing dirs in {q_dir.name}")
        return

    out_dir = results_root / q_dir.name
    out_dir.mkdir(parents=True, exist_ok=True)
    cache_file = out_dir / "gemma4_loc_cache.jsonl"

    # Load already-computed entries if resuming
    done: set[str] = set()
    if resume and cache_file.exists():
        for line in cache_file.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done.add(json.loads(line)["submission"])
        print(f"  Resuming: {len(done)} already cached")

    submissions = sorted(wrong_dir.glob("wrong_*.py"))
    desc_path = q_dir / "description.txt"

    with cache_file.open("a", encoding="utf-8") as f:
        for i, sub in enumerate(submissions, 1):
            if sub.name in done:
                continue

            program = Program(
                submission_path=sub,
                test_suite_path=test_suite,
                description_path=desc_path if desc_path.exists() else None,
            )

            result = run_tests(sub, test_suite)

            if result["has_syntax_error"] or result["timed_out"] or result["solved"]:
                suspicious_lines = None
                reason = (
                    "syntax_error" if result["has_syntax_error"]
                    else "timed_out" if result["timed_out"]
                    else "already_solved"
                )
                print(f"  [{i}/{len(submissions)}] {sub.name}: skip ({reason})")
            else:
                loc_prompt = build_localization_prompt(
                    program.get_student_code(), result["failing_tests"]
                )
                suspicious_lines = llm.generate(loc_prompt)
                preview = suspicious_lines[:60].replace("\n", " ")
                print(f"  [{i}/{len(submissions)}] {sub.name}: {preview}…")

            record = {
                "submission": sub.name,
                "suspicious_lines": suspicious_lines,
            }
            f.write(json.dumps(record) + "\n")
            f.flush()


def main() -> None:
    parser = argparse.ArgumentParser(description="Pre-compute Gemma4 localization cache.")
    parser.add_argument("--questions-root", required=True)
    parser.add_argument("--results-root", required=True)
    parser.add_argument("--questions", nargs="+", type=int, default=[1, 2, 3, 4, 5])
    parser.add_argument("--resume", action="store_true",
                        help="Skip submissions already in the cache file.")
    args = parser.parse_args()

    questions_root = Path(args.questions_root)
    results_root = Path(args.results_root)

    print("Loading Gemma4 for localization …")
    llm = Gemma4LLM()
    print("Gemma4 loaded.\n")

    for n in args.questions:
        q_dir = questions_root / f"question_{n}"
        if not q_dir.exists():
            print(f"[skip] question_{n} not found")
            continue
        print(f"\n=== question_{n} ===")
        precompute_question(q_dir, llm, results_root, resume=args.resume)

    print("\nDone. Cache files saved to:", results_root)


if __name__ == "__main__":
    main()
