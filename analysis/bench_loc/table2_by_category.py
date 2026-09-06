"""
Minimal set F1 on Bench, broken down by injected-bug category.

Extends table1_minimal_set_llm.py: instead of one F1 per model averaged
over all submissions, this splits F1 by Data_Bench's injected-bug category
(syntax error, logic error, reference error, multiple error) per model.
This has no Refactory equivalent -- Refactory submissions aren't tagged
with a bug category -- so it's a Bench-only view of *where* each method's
minimal-set accuracy holds up or collapses.
"""

from __future__ import annotations

from common import MODELS, MODEL_LABELS, OUT_TABLES, load_ground_truth, load_metadata
from table1_minimal_set_llm import build_table1

import numpy as np
import pandas as pd


def build_table2(per_model_scores: dict, meta: dict) -> pd.DataFrame:
    rows = []
    for key, label in [("fauxpy", "FauxPy")] + [(m, MODEL_LABELS[m]) for m in MODELS]:
        scores = per_model_scores[key]
        by_cat: dict[str, list[float]] = {}
        for name, (p, r, f1) in scores.items():
            cat = meta.get(name, "unknown")
            by_cat.setdefault(cat, []).append(f1)
        row = {"Method": label}
        for cat, f1s in by_cat.items():
            row[cat] = np.mean(f1s)
        rows.append(row)
    return pd.DataFrame(rows).set_index("Method")


if __name__ == "__main__":
    gt = load_ground_truth()
    meta = load_metadata()
    _, per_model_scores = build_table1(gt)

    print("Minimal set F1 on Bench, by injected-bug category\n")
    table2 = build_table2(per_model_scores, meta).round(3)
    print(table2.to_string())

    csv_path = OUT_TABLES / "table2_bench_minimal_set_by_category.csv"
    table2.to_csv(csv_path)
    print(f"\n[saved] {csv_path}")