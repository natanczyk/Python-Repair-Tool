"""
Figure 2. Top-k localization

Grouped bar chart: Top-1, Top-3, Top-6 for every method. No heatmaps.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

from table1_localization import build_table1

OUT_DIR = Path(__file__).parent / "figures"
OUT_DIR.mkdir(exist_ok=True)

FAUXPY_COLOR = "#E07B39"


def main():
    table1 = build_table1().round(3)
    methods = list(table1.index)

    x = np.arange(len(methods))
    width = 0.26

    fig, ax = plt.subplots(figsize=(13, 5.5))
    ax.bar(x - width, table1["Top-1"].tolist(), width, label="Top-1", color="#4878CF", alpha=0.88)
    ax.bar(x,         table1["Top-3"].tolist(), width, label="Top-3", color="#6ACC65", alpha=0.88)
    ax.bar(x + width, table1["Top-6"].tolist(), width, label="Top-6", color="#D65F5F", alpha=0.88)

    fauxpy_idx = [i for i, m in enumerate(methods) if "FauxPy" in m]
    for i in fauxpy_idx:
        ax.axvspan(i - 0.4, i + 0.4, color=FAUXPY_COLOR, alpha=0.07, zorder=0)

    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=30, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("Score")
    ax.set_title("Top-k Localization: Top-1 / Top-3 / Top-6")
    ax.legend(fontsize=9, ncol=3, loc="upper left")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig_path = OUT_DIR / "figure2_topk_localization.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()
