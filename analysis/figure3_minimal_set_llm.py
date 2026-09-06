"""
Figure for Table 3: Minimal set accuracy using actual LLM minimal-set
predictions (with tests) vs FauxPy top-|GT|.

F1 only, one bar per method.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

from table3_minimal_set_llm import build_table3

OUT_DIR = Path(__file__).parent / "figures"
OUT_DIR.mkdir(exist_ok=True)

FAUXPY_COLOR = "#E07B39"


def main():
    table3 = build_table3().round(3)
    methods = list(table3.index)

    x = np.arange(len(methods))

    fig, ax = plt.subplots(figsize=(13, 5.5))

    bars = ax.bar(x, table3["F1"].tolist(), 0.6, color="#D65F5F", alpha=0.88)
    for bar, v in zip(bars, table3["F1"].tolist()):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f"{v:.3f}", ha="center", va="bottom", fontsize=9)

    fauxpy_idx = [i for i, m in enumerate(methods) if "FauxPy" in m]
    for i in fauxpy_idx:
        ax.axvspan(i - 0.4, i + 0.4, color=FAUXPY_COLOR, alpha=0.07, zorder=0)

    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=30, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("Score")
    ax.set_title("Minimal Set Accuracy: LLM Minimal-Set Predictions (with tests) vs FauxPy top-|GT|")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig_path = OUT_DIR / "figure3_minimal_set_llm.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()
