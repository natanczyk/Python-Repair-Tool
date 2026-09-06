"""
Table 7. Does solve rate degrade as the actual bug gets more complex?
Stratifies solve rate by the number of ground-truth buggy lines per
submission, on the comparable 4-question basis, pooled across all 8 models.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

from common import OUT_TABLES, OUT_FIGURES, load_records, comparable, load_ground_truth_sizes


def bucket_size(n: int) -> str:
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    if n <= 3:
        return "2-3"
    if n <= 6:
        return "4-6"
    return "7+"


ORDER = ["0", "1", "2-3", "4-6", "7+"]


def build_table7() -> tuple[pd.DataFrame, pd.Series]:
    df = comparable(load_records())
    sizes = load_ground_truth_sizes()
    df["gt_size"] = df.apply(lambda r: sizes.get((r["question"], r["submission"])), axis=1)
    df = df.dropna(subset=["gt_size"])
    df["bucket"] = df["gt_size"].astype(int).apply(bucket_size)

    pivot = df.groupby(["bucket", "repair_type"])["solved"].mean().unstack()
    pivot = pivot.reindex(index=ORDER)
    n = df.groupby("bucket").size().reindex(ORDER)
    return pivot, n


def main():
    table7, n = build_table7()
    table7 = table7.round(3)
    print("Solve rate by ground-truth bug-set size (all 8 models pooled, questions 1,3,4,5)\n")
    print(table7.to_string())
    print("\nn per bucket:")
    print(n.to_string())
    table7.to_csv(OUT_TABLES / "table7_difficulty.csv")
    print(f"\n[saved] {OUT_TABLES / 'table7_difficulty.csv'}")

    fig, ax = plt.subplots(figsize=(9, 5.5))
    colors = {"none": "#8B8378", "fauxpy": "#E07B39", "best_loc": "#4878CF", "self_llm": "#6ACC65"}
    for t in table7.columns:
        ax.plot(table7.index, table7[t], marker="o", label=t, color=colors.get(t, None), linewidth=2)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_xlabel("Ground-truth buggy-line count")
    ax.set_ylabel("Solve rate")
    ax.set_title("Solve Rate vs. Bug Complexity (all models pooled)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure7_difficulty.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()