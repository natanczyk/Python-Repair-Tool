"""
Shared constants and data loading for the QuixBugs localization analysis.
Mirrors the top-level Refactory table1/2/3/5 scripts' logic exactly, just
pointed at Data_QuixBugs / results_v2/quixbugs_loc and 40 questions instead
of Data / results_v2/refactory_loc and 5.

Unlike Refactory's per-question-folder layout, results_v2/quixbugs_loc/
holds localization results already merged into one flat file per
(mode, model) combination (e.g. llm_gemma4_minimal_notests_localization.jsonl)
rather than split across question_N/ subfolders -- load_ranking() and
load_llm_minimal_set() read those directly. Data_QuixBugs/ itself (ground
truth) is untouched and still per-question, since that's the canonical
dataset layout shared with the repair pipeline.

Note: only 31 of the 40 questions have an ans/ folder (test I/O pairs) --
the other 9 are graph/linked-list programs whose test suites were adapted
from hand-written pytest files instead of generated from JSON test data.
ranking and minimal_tests therefore only ever have ~31 comparable programs;
minimal_notests and fauxpy have all 40. This falls out naturally from the
existing dict-membership filtering (`if name in ranking`, etc.) -- no
special-casing needed, but sample sizes (n) will differ by method/mode and
are much smaller than Refactory's throughout (40 programs vs. 1,783
submissions), since QuixBugs is one program per question, not many student
submissions per question.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT       = Path(__file__).parent.parent.parent
QUIX_LOC   = ROOT / "results_v2" / "quixbugs_loc"
DATA_QUIX  = ROOT / "Data_QuixBugs"
OUT_TABLES  = Path(__file__).parent / "tables"
OUT_FIGURES = Path(__file__).parent / "figures"
OUT_TABLES.mkdir(exist_ok=True)
OUT_FIGURES.mkdir(exist_ok=True)

QUESTIONS = list(range(1, 41))

MODELS = [
    "qwen", "qwen3_27b", "qwen3_coder", "gemma4",
    "granite4", "codegemma", "granite_code", "codellama",
]

MODEL_LABELS = {
    "qwen":         "Qwen2.5",
    "qwen3_27b":    "Qwen3.6",
    "qwen3_coder":  "Qwen3Coder",
    "gemma4":       "Gemma4",
    "granite4":     "Granite4",
    "codegemma":    "CodeGemma",
    "granite_code": "GraniteCode",
    "codellama":    "CodeLlama",
}


def load_jsonl(path: Path) -> dict[str, list[int]]:
    if not path.exists():
        return {}
    data = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            data[r["program_name"]] = r["buggy_lines"]
    return data


def load_ground_truth() -> dict[str, list[int]]:
    gt = {}
    for q in QUESTIONS:
        gt.update(load_jsonl(DATA_QUIX / f"question_{q}" / "ground_truth.jsonl"))
    return gt


def load_ranking(method: str) -> dict[str, list[int]]:
    fname = "fauxpy_localization.jsonl" if method == "fauxpy" else f"llm_{method}_localization.jsonl"
    return load_jsonl(QUIX_LOC / fname)


def load_llm_minimal_set(model: str, with_tests: bool) -> dict[str, list[int]]:
    suffix = "minimal_localization" if with_tests else "minimal_notests_localization"
    return load_jsonl(QUIX_LOC / f"llm_{model}_{suffix}.jsonl")


def prf(pred_set: set[int], gt_set: set[int]) -> tuple[float, float, float]:
    if not pred_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gt_set)
    p = tp / len(pred_set)
    r = tp / len(gt_set)
    f1 = (2 * p * r / (p + r)) if (p + r) > 0 else 0.0
    return p, r, f1