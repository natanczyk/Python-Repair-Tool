"""
Minimal set accuracy on QuixBugs (actual LLM minimal-set predictions) --
direct parallel to table3_minimal_set_llm.py (Refactory).

Unlike Table 1 (which derives a "minimal set" for LLMs by slicing their
ranking to the top-|GT| lines), this table uses the LLMs' own minimal-set
predictions directly: llm_<model>_minimal_localization.jsonl (model given
failing test output and asked to name the exact set of buggy lines).

FauxPy has no minimal-set prediction mode, so its predicted set is the
top-k lines of its ranking, k = size of ground truth for that program.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from common import MODELS, MODEL_LABELS, OUT_TABLES, load_ground_truth, load_ranking, load_llm_minimal_set, prf


def compute_fauxpy_metrics(gt: dict) -> dict:
    ranking = load_ranking("fauxpy")
    common = [name for name in gt if name in ranking]
    precs, recs, f1s = [], [], []
    for name in common:
        gt_set = set(gt[name])
        if not gt_set:
            continue
        pred_set = set(ranking[name][:len(gt_set)])
        p, r, f1 = prf(pred_set, gt_set)
        precs.append(p)
        recs.append(r)
        f1s.append(f1)
    return {
        "n": len(precs),
        "Precision": np.mean(precs) if precs else 0.0,
        "Recall":    np.mean(recs) if recs else 0.0,
        "F1":        np.mean(f1s) if f1s else 0.0,
    }


def compute_llm_metrics(gt: dict, model: str) -> dict:
    preds = load_llm_minimal_set(model, with_tests=True)
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
        "n": len(precs),
        "Precision": np.mean(precs) if precs else 0.0,
        "Recall":    np.mean(recs) if recs else 0.0,
        "F1":        np.mean(f1s) if f1s else 0.0,
    }


def build_table3() -> pd.DataFrame:
    gt = load_ground_truth()
    rows = []

    fauxpy_metrics = compute_fauxpy_metrics(gt)
    rows.append({"Method": "FauxPy", **{k: v for k, v in fauxpy_metrics.items() if k != "n"}})

    for model in MODELS:
        metrics = compute_llm_metrics(gt, model)
        rows.append({"Method": MODEL_LABELS[model], **{k: v for k, v in metrics.items() if k != "n"}})

    return pd.DataFrame(rows).set_index("Method")


if __name__ == "__main__":
    gt = load_ground_truth()
    table3 = build_table3().round(3)

    print(f"Minimal set accuracy: LLM minimal-set predictions (with tests) vs FauxPy top-|GT|")
    print(f"Ground truth: {len(gt)} QuixBugs programs (questions 1-40)\n")
    print(table3.to_string())

    csv_path = OUT_TABLES / "table3_minimal_set_llm.csv"
    table3.to_csv(csv_path)
    print(f"\n[saved] {csv_path}")