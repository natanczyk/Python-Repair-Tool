"""
Figure for Table 1: Minimal set accuracy on Bench (LLM minimal_notests vs
FauxPy top-|GT|). F1 only, one bar per method -- same style as
figure3_minimal_set_llm.py (the Refactory equivalent).
"""

from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

from common import OUT_FIGURES, load_ground_truth
from table1_minimal_set_llm import build_table1

def main():
    gt = load_ground_truth()
    table1, _ = build_table1(gt)
    table1 = table1.round(3)
    table1 = table1[table1.index != "FauxPy"]
    methods = list(table1.index)

    x = np.arange(len(methods))

    fig, ax = plt.subplots(figsize=(13, 5.5))

    bars = ax.bar(x, table1["F1"].tolist(), 0.6, color="#D65F5F", alpha=0.88)
    for bar, v in zip(bars, table1["F1"].tolist()):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f"{v:.3f}", ha="center", va="bottom", fontsize=9)

    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=30, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("Score")
    ax.set_title("Minimal Set Accuracy (Bench): LLM Minimal-Set Predictions (no tests)")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure1_bench_minimal_set_llm.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()