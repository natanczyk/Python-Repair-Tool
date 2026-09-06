"""
Run repair-loop experiments on the Refactory dataset.

Four repair types:
  none      — no localization; code + failing tests only
  fauxpy    — FauxPy Ochiai scores provided at each iteration
  best_loc  — Gemma4 pre-computed localization (static); requires gemma4_loc_cache.jsonl
  self_llm  — same model first localizes, then repairs, at each iteration

Results (one file per type × model):
  <results_root>/question_N/repair_<type>_<model>_results.jsonl

Each line:
  {"submission": "wrong_1_001.py", "solved": true/false, "iterations": N,
   "repair_type": "none", "repair_model": "qwen"}

Repaired code for solved submissions:
  <results_root>/question_N/repaired_<type>_<model>/wrong_N_XXX.py

Usage:
  python repair_research/run_repair.py \\
    --repair-type none \\
    --repair-model qwen \\
    --questions-root /home/guests3/nkg/MASTER_PROJECT/Data \\
    --results-root /media/generalstorage4/nkgstorage/Results/repair

  # best_loc requires the Gemma4 cache to exist first:
  python repair_research/precompute_loc.py --questions-root ... --results-root ...
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



def run_question(
    repair_type: str,
    repair_model: str,
    q_dir: Path,
    llm,
    results_root: Path,
    resume: bool,
    loc_llm=None,
    max_attempts: int = 4,
) -> None:
    wrong_dir = q_dir / "code" / "wrong"
    test_suite = q_dir / "test_suite.py"
    desc_path = q_dir / "description.txt"

    if not wrong_dir.exists() or not test_suite.exists():
        print(f"  [skip] missing dirs in {q_dir.name}")
        return

    out_dir = results_root / q_dir.name
    out_dir.mkdir(parents=True, exist_ok=True)
    results_file = out_dir / f"repair_{repair_type}_{repair_model}_results.jsonl"
    repaired_dir = out_dir / f"repaired_{repair_type}_{repair_model}"
    repaired_dir.mkdir(exist_ok=True)

    # Load already-done submissions when resuming
    done: set[str] = set()
    if resume and results_file.exists():
        for line in results_file.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done.add(Path(json.loads(line)["submission"]).name)
        print(f"  Resuming: {len(done)} already recorded")

    submissions = sorted(wrong_dir.glob("wrong_*.py"))
    print(f"  {len(submissions)} submissions → {results_file}")

    with results_file.open("a", encoding="utf-8") as f:
        for i, sub in enumerate(submissions, 1):
            if sub.name in done:
                continue

            program = Program(
                submission_path=sub,
                test_suite_path=test_suite,
                description_path=desc_path if desc_path.exists() else None,
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

            # Save repaired code for solved submissions
            if agent.solved and agent.final_code:
                (repaired_dir / sub.name).write_text(agent.final_code, encoding="utf-8")

            record = {
                "submission": sub.name,
                "solved": agent.solved,
                "iterations": agent.iterations,
                "repair_type": repair_type,
                "repair_model": repair_model,
            }
            f.write(json.dumps(record) + "\n")
            f.flush()

            status = "solved" if agent.solved else "failed"
            print(f"  [{i}/{len(submissions)}] {sub.name}: {status} in {agent.iterations} iter(s)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run repair-loop experiments.")
    parser.add_argument("--repair-type", required=True, choices=_REPAIR_TYPES)
    parser.add_argument("--repair-model", required=True, choices=_MODEL_CHOICES)
    parser.add_argument("--questions-root", required=True)
    parser.add_argument("--results-root", required=True)
    parser.add_argument("--questions", nargs="+", type=int, default=[1, 2, 3, 4, 5])
    parser.add_argument("--max-attempts", type=int, default=4)
    parser.add_argument("--resume", action="store_true",
                        help="Skip submissions already recorded in the results file.")
    args = parser.parse_args()

    questions_root = Path(args.questions_root)
    results_root = Path(args.results_root)

    print(f"Loading model '{args.repair_model}' …")
    llm = _build_llm(args.repair_model)
    print(f"Model loaded.\n")

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
    print(f"  MAX ATTEMPTS : {args.max_attempts}")
    print(f"{'='*55}")

    for n in args.questions:
        q_dir = questions_root / f"question_{n}"
        if not q_dir.exists():
            print(f"\n[skip] question_{n}: folder not found")
            continue
        print(f"\n=== question_{n} ===")
        run_question(
            repair_type=args.repair_type,
            repair_model=args.repair_model,
            q_dir=q_dir,
            llm=llm,
            results_root=results_root,
            resume=args.resume,
            loc_llm=loc_llm,
            max_attempts=args.max_attempts,
        )

    print(f"\nDone. Results saved to: {results_root}")


if __name__ == "__main__":
    main()
