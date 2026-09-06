"""
Table 5. Minimal set detection: with tests vs. without tests

Compares each LLM's own minimal-set prediction under two prompting
conditions:
    with tests:    llm_<model>_minimal_localization.jsonl
                   (model sees failing test input/output pairs)
    without tests: llm_<model>_minimal_notests_localization.jsonl
                   (model sees only the assignment description and code)

Both are compared directly against ground truth with set-based
Precision / Recall / F1 (no top-k slicing - these are the model's own
predicted sets, exactly as in Table 3).
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT      = Path(__file__).parent.parent
REF_LOC   = ROOT / "results_v2" / "refactory_loc"
DATA      = ROOT / "Data"
OUT_DIR   = Path(__file__).parent / "tables"
OUT_DIR.mkdir(exist_ok=True)

QUESTIONS = [1, 2, 3, 4, 5]

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
        gt.update(load_jsonl(DATA / f"question_{q}" / "ground_truth.jsonl"))
    return gt


def load_llm_minimal_set(model: str, with_tests: bool) -> dict[str, list[int]]:
    suffix = "minimal_localization" if with_tests else "minimal_notests_localization"
    preds = {}
    for q in QUESTIONS:
        preds.update(load_jsonl(REF_LOC / f"question_{q}" / f"llm_{model}_{suffix}.jsonl"))
    return preds


def prf(pred_set: set[int], gt_set: set[int]) -> tuple[float, float, float]:
    if not pred_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gt_set)
    p = tp / len(pred_set)
    r = tp / len(gt_set)
    f1 = (2 * p * r / (p + r)) if (p + r) > 0 else 0.0
    return p, r, f1


def compute_metrics(gt: dict, preds: dict) -> dict:
    common = [name for name in gt if name in preds]
    precs, recs, f1s = [], [], []
    for name in common:
        gt_set = set(gt[name])
        if not gt_set:
            continue
        pred_set = set(preds[name])
        p, r, f1 = prf(pred_set, gt_set)
        precs.append(p)
        recs.append(r)
        f1s.append(f1)
    return {
        "n":         len(precs),
        "Precision": np.mean(precs) if precs else 0.0,
        "Recall":    np.mean(recs) if recs else 0.0,
        "F1":        np.mean(f1s) if f1s else 0.0,
    }


def build_table5() -> pd.DataFrame:
    gt = load_ground_truth()
    rows = []
    for model in MODELS:
        with_tests = compute_metrics(gt, load_llm_minimal_set(model, with_tests=True))
        no_tests   = compute_metrics(gt, load_llm_minimal_set(model, with_tests=False))
        rows.append({
            "Method":                  MODEL_LABELS[model],
            "F1 (with tests)":         with_tests["F1"],
            "F1 (without tests)":      no_tests["F1"],
            "Precision (with tests)":  with_tests["Precision"],
            "Precision (without tests)": no_tests["Precision"],
            "Recall (with tests)":     with_tests["Recall"],
            "Recall (without tests)":  no_tests["Recall"],
        })
    return pd.DataFrame(rows).set_index("Method")


if __name__ == "__main__":
    gt = load_ground_truth()
    table5 = build_table5().round(3)

    print(f"Minimal set detection: with tests vs without tests (Refactory, n={len(gt)})\n")
    print(table5.to_string())

    csv_path = OUT_DIR / "table5_minimal_set_tests_vs_notests.csv"
    table5.to_csv(csv_path)
    print(f"\n[saved] {csv_path}")
