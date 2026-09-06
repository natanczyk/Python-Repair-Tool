"""
Figure 1. Minimal set accuracy

For every method, take the top-k suspicious lines (k = size of that
submission's ground-truth bug set) and compare against ground truth with F1.
For FauxPy this means taking its first k suspicious lines, exactly as
described for Table 1. Answers: "Which method finds the correct buggy lines?"
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from table1_localization import build_table1

OUT_DIR = Path(__file__).parent / "figures"
OUT_DIR.mkdir(exist_ok=True)

FAUXPY_COLOR = "#E07B39"
LLM_COLOR    = "#4878CF"


def main():
    table1 = build_table1().round(3)
    methods = list(table1.index)
    f1_vals = table1["Minimal Set F1"].tolist()
    colors  = [FAUXPY_COLOR if "FauxPy" in m else LLM_COLOR for m in methods]

    fig, ax = plt.subplots(figsize=(12, 5.5))
    bars = ax.bar(methods, f1_vals, color=colors, alpha=0.88)
    for bar, v in zip(bars, f1_vals):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f"{v:.3f}", ha="center", va="bottom", fontsize=9)

    ax.set_xticks(range(len(methods)))
    ax.set_xticklabels(methods, rotation=30, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("F1-score")
    ax.set_title("Minimal Set Accuracy (top-|GT| lines vs. ground truth)")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig_path = OUT_DIR / "figure1_minimal_set_accuracy.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()
