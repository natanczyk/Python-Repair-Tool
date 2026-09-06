"""
Minimal set detection on QuixBugs: with tests vs. without tests -- direct
parallel to table5_minimal_set_tests_vs_notests.py (Refactory).

Compares each LLM's own minimal-set prediction under two prompting
conditions:
    with tests:    llm_<model>_minimal_localization.jsonl
    without tests: llm_<model>_minimal_notests_localization.jsonl

Both are compared directly against ground truth with set-based
Precision / Recall / F1.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from common import MODELS, MODEL_LABELS, OUT_TABLES, load_ground_truth, load_llm_minimal_set, prf


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

    print(f"Minimal set detection: with tests vs without tests (QuixBugs, n={len(gt)})\n")
    print(table5.to_string())

    csv_path = OUT_TABLES / "table5_minimal_set_tests_vs_notests.csv"
    table5.to_csv(csv_path)
    print(f"\n[saved] {csv_path}")