"""
Smoke test for faulty_lines_finder.py — runs both fauxpy and llm methods on a
single known buggy submission (wrong_1_001.py from question_1) and saves the
results to test_notebooks/test_results/.

Run from the project root with the venv active:
    python test_notebooks/test_faulty_lines_finder.py

NOTE: The LLM test requires a GPU. If no GPU is detected it is skipped
      automatically — run the full test on the server.
"""

from __future__ import annotations

import importlib.util
import json
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# faulty_lines_finder lives in a folder whose name contains a space
_spec = importlib.util.spec_from_file_location(
    "faulty_lines_finder",
    PROJECT_ROOT / "Faulty_Lines_and_Repair_research" / "faulty_lines_finder.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
run_fauxpy_localization = _mod.run_fauxpy_localization
run_llm_localization    = _mod.run_llm_localization

Q1_DIR       = PROJECT_ROOT / "Data" / "question_1"
TEST_SUITE   = Q1_DIR / "test_suite.py"
ANS_DIR      = Q1_DIR / "ans"
DESC_PATH    = Q1_DIR / "description.txt"
SUBMISSION   = Q1_DIR / "code" / "wrong" / "wrong_1_001.py"

RESULTS_DIR  = Path(__file__).parent / "test_results"
RESULTS_DIR.mkdir(exist_ok=True)

description_path = DESC_PATH if DESC_PATH.exists() else None


def run_fauxpy_test():
    print("\n--- FauxPy ---")
    print(f"Submission : {SUBMISSION.name}")
    print(f"Test suite : {TEST_SUITE}")

    tmp_dir = RESULTS_DIR / "fauxpy_tmp"
    tmp_dir.mkdir(exist_ok=True)
    shutil.copy(SUBMISSION, tmp_dir / SUBMISSION.name)

    output_file = RESULTS_DIR / "fauxpy_result.jsonl"
    run_fauxpy_localization(
        wrong_dir=tmp_dir,
        test_suite_path=TEST_SUITE,
        output_file=output_file,
        description_path=description_path,
    )

    record = json.loads(output_file.read_text(encoding="utf-8").strip())
    print(f"Result     : {record}")
    print(f"Saved to   : {output_file}")
    return record


def run_llm_test():
    import torch
    if not torch.cuda.is_available():
        print("\n--- LLM (QwenLLM) ---")
        print("SKIPPED: no GPU detected on this machine.")
        print("Run this test on the server where QwenLLM is available.")
        return None

    print("\n--- LLM (QwenLLM) ---")
    print(f"Submission : {SUBMISSION.name}")
    print(f"ans/       : {ANS_DIR}")
    print("Loading QwenLLM ...")

    from LLMs.llm import QwenLLM
    llm = QwenLLM()
    print("Model loaded.")

    tmp_dir = RESULTS_DIR / "llm_tmp"
    tmp_dir.mkdir(exist_ok=True)
    shutil.copy(SUBMISSION, tmp_dir / SUBMISSION.name)

    output_file = RESULTS_DIR / "llm_result.jsonl"
    run_llm_localization(
        wrong_dir=tmp_dir,
        ans_dir=ANS_DIR,
        output_file=output_file,
        llm=llm,
        mode="ranking",
        description_path=description_path,
    )

    record = json.loads(output_file.read_text(encoding="utf-8").strip())
    print(f"Result     : {record}")
    print(f"Saved to   : {output_file}")
    return record


if __name__ == "__main__":
    fauxpy_record = run_fauxpy_test()
    llm_record    = run_llm_test()

    print("\n=== Summary ===")
    print(f"FauxPy suspicious lines : {fauxpy_record['buggy_lines']}")
    print(f"LLM suspicious lines    : {llm_record['buggy_lines'] if llm_record else 'skipped (no GPU)'}")
    print("(known bug is on line 3: 'x < e' should be 'x <= e')")
    print(f"\nResults saved in: {RESULTS_DIR}")
