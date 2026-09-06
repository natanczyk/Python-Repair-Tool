"""
Outcome taxonomy on QuixBugs over ALL submissions (not just failures) --
direct parallel to table5_failure_taxonomy.py (Refactory). Categories are
mutually exclusive and always sum to 100% of the (questions x types x
models) basis:

  already passing (solved, 0 iter)     -- original code already passed; no
                                           repair was needed or attempted
  solved with repair (solved, 1+ iter) -- a real repair happened
  never attempted (unsolved, 0 iter)   -- timeout/crash on the very first
                                           check; no repair attempt possible
  died mid-loop (unsolved, 1-3 iter)   -- a later-iteration timeout/crash
  exhausted budget (unsolved, 4 iter)  -- genuinely tried and failed
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

from common import (
    OUT_TABLES, OUT_FIGURES, MODELS, TYPES, MODEL_LABELS, TYPE_LABELS,
    MAX_ATTEMPTS, load_records, comparable,
)

CATEGORIES = [
    "already passing (solved, 0 iter)",
    "solved with repair (solved, 1+ iter)",
    "never attempted (unsolved, 0 iter)",
    "died mid-loop (unsolved, 1-3 iter)",
    "exhausted budget (unsolved, 4 iter)",
]


def categorize(row) -> str:
    solved, it = row["solved"], row["iterations"]
    if solved and it == 0:
        return CATEGORIES[0]
    if solved:
        return CATEGORIES[1]
    if it == 0:
        return CATEGORIES[2]
    if it >= MAX_ATTEMPTS:
        return CATEGORIES[4]
    return CATEGORIES[3]


def build_table5() -> pd.DataFrame:
    df = comparable(load_records())
    df["category"] = df.apply(categorize, axis=1)
    counts = df.groupby(["repair_model", "repair_type", "category"]).size().unstack(fill_value=0)
    props = counts.div(counts.sum(axis=1), axis=0)
    props = props.reindex(columns=CATEGORIES, fill_value=0.0)
    return props


def main():
    table5_raw = build_table5()
    row_sums = table5_raw.sum(axis=1)
    assert np.allclose(row_sums, 1.0), f"Rows don't sum to 1: {row_sums[~np.isclose(row_sums, 1.0)]}"

    table5 = table5_raw.round(3)
    table5.index = pd.MultiIndex.from_tuples(
        [(MODEL_LABELS[m], TYPE_LABELS[t]) for m, t in table5.index],
        names=["Model", "Type"],
    )
    print("Outcome taxonomy, share of ALL submissions per cell (QuixBugs, questions 1-40)\n")
    print(table5.to_string())
    table5.to_csv(OUT_TABLES / "table5_failure_taxonomy.csv")
    print(f"\n[saved] {OUT_TABLES / 'table5_failure_taxonomy.csv'}")

    # Figure: stacked bars, aggregated by repair type (all models pooled)
    df = comparable(load_records())
    df["category"] = df.apply(categorize, axis=1)
    by_type = df.groupby(["repair_type", "category"]).size().unstack(fill_value=0)
    by_type = by_type.reindex(index=TYPES, columns=CATEGORIES, fill_value=0)
    by_type_prop = by_type.div(by_type.sum(axis=1), axis=0)

    fig, ax = plt.subplots(figsize=(9.5, 6))
    labels = [TYPE_LABELS[t] for t in TYPES]
    bottoms = np.zeros(len(labels))
    colors = ["#B8D8B0", "#4878CF", "#D65F5F", "#E8C15C", "#8B8378"]
    for col, color in zip(by_type_prop.columns, colors):
        vals = by_type_prop[col].tolist()
        ax.bar(labels, vals, bottom=bottoms, label=col, color=color, alpha=0.9)
        bottoms += np.array(vals)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("Share of all submissions")
    ax.set_title("Outcome Taxonomy by Repair Type (QuixBugs, all models pooled)")
    ax.legend(fontsize=8.5, loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=1)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure5_failure_taxonomy.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()