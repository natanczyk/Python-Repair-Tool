"""
Overall localization performance on QuixBugs -- direct parallel to
table1_localization.py (Refactory).

For every method, the full predicted ranking of source lines is evaluated
against ground truth on QuixBugs (questions 1-40):

  Top-1 / Top-3 / Top-6   - proportion of programs where at least one
                            ground-truth buggy line appears in the top-k
                            of the ranking (fault-localization hit-rate).
  MRR                     - mean reciprocal rank of the first correct line
                            (0 if never retrieved).
  Minimal Set P/R/F1      - the top-|GT| lines of the ranking are taken as
                            the predicted minimal bug set and compared to
                            ground truth with set-based Precision/Recall/F1.
                            Applied identically to FauxPy and every LLM.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from common import MODELS, MODEL_LABELS, OUT_TABLES, load_ground_truth, load_ranking


def compute_method_metrics(gt: dict, ranking: dict) -> dict:
    common = [name for name in gt if name in ranking]
    p_at = {1: [], 3: [], 6: []}
    rr = []
    precs, recs, f1s = [], [], []

    for name in common:
        gt_set = set(gt[name])
        if not gt_set:
            continue
        pred = ranking[name]

        for k in (1, 3, 6):
            p_at[k].append(1.0 if set(pred[:k]) & gt_set else 0.0)

        rank = next((i for i, line in enumerate(pred, 1) if line in gt_set), None)
        rr.append(1.0 / rank if rank else 0.0)

        pred_set = set(pred[:len(gt_set)])
        tp = len(pred_set & gt_set)
        p = tp / len(pred_set) if pred_set else 0.0
        r = tp / len(gt_set)
        f1 = (2 * p * r / (p + r)) if (p + r) > 0 else 0.0
        precs.append(p)
        recs.append(r)
        f1s.append(f1)

    return {
        "n":                      len(precs),
        "Top-1":                  np.mean(p_at[1]) if p_at[1] else 0.0,
        "Top-3":                  np.mean(p_at[3]) if p_at[3] else 0.0,
        "Top-6":                  np.mean(p_at[6]) if p_at[6] else 0.0,
        "MRR":                    np.mean(rr) if rr else 0.0,
        "Minimal Set Precision":  np.mean(precs) if precs else 0.0,
        "Minimal Set Recall":     np.mean(recs) if recs else 0.0,
        "Minimal Set F1":         np.mean(f1s) if f1s else 0.0,
    }


def build_table1() -> pd.DataFrame:
    gt = load_ground_truth()
    methods = ["fauxpy"] + MODELS

    rows = []
    for m in methods:
        ranking = load_ranking(m)
        metrics = compute_method_metrics(gt, ranking)
        label = "FauxPy (SBFL)" if m == "fauxpy" else MODEL_LABELS[m]
        rows.append({"Method": label, **{k: v for k, v in metrics.items() if k != "n"}})

    return pd.DataFrame(rows).set_index("Method")


if __name__ == "__main__":
    gt = load_ground_truth()
    table1 = build_table1().round(3)

    print(f"Evaluated on {len(gt)} QuixBugs programs (questions 1-40, ground-truth non-empty only)\n")
    print(table1.to_string())

    csv_path = OUT_TABLES / "table1_localization.csv"
    table1.to_csv(csv_path)
    print(f"\n[saved] {csv_path}")