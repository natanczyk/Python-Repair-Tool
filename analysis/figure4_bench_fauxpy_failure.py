"""
Figure for Table 4: FauxPy empty-prediction rate by injected-bug category
on the Bench dataset. One bar per category, no heatmap.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

from table4_bench_fauxpy_failure import build_category_table

OUT_DIR = Path(__file__).parent / "figures"
OUT_DIR.mkdir(exist_ok=True)


def main():
    cat_table = build_category_table()
    categories = [c.replace(" ", "\n") for c in cat_table.index]
    rates = cat_table["Empty rate"].tolist()

    fig, ax = plt.subplots(figsize=(9, 5.5))
    bars = ax.bar(categories, rates, color="#D65F5F", alpha=0.88)
    for bar, v in zip(bars, rates):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f"{v:.1%}", ha="center", va="bottom", fontsize=10)

    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("FauxPy empty-prediction rate")
    ax.set_title("FauxPy Empty Predictions by Injected-Bug Category (Bench)")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig_path = OUT_DIR / "figure4_bench_fauxpy_failure.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()
