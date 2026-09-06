"""
Figure for Table 2: Minimal set F1 on Bench, grouped bar chart per model
with one bar per injected-bug category. Bench-only view (no Refactory
equivalent) of where each method's accuracy holds up or collapses.
"""

from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

from common import OUT_FIGURES, load_ground_truth, load_metadata
from table1_minimal_set_llm import build_table1
from table2_by_category import build_table2

CATEGORY_COLORS = {
    "syntax error":    "#D65F5F",
    "logic error":     "#4878CF",
    "reference error": "#6ACC65",
    "multiple error":  "#8064A2",
}


def main():
    gt = load_ground_truth()
    meta = load_metadata()
    _, per_model_scores = build_table1(gt)
    table2 = build_table2(per_model_scores, meta).round(3)

    methods = list(table2.index)
    categories = [c for c in table2.columns if c in CATEGORY_COLORS] + \
                 [c for c in table2.columns if c not in CATEGORY_COLORS]

    x = np.arange(len(methods))
    n = len(categories)
    width = 0.8 / n

    fig, ax = plt.subplots(figsize=(14, 5.5))
    for i, cat in enumerate(categories):
        vals = table2[cat].fillna(0).tolist()
        offset = (i - (n - 1) / 2) * width
        ax.bar(x + offset, vals, width, label=cat.capitalize(),
               color=CATEGORY_COLORS.get(cat, "#888888"), alpha=0.88)

    fauxpy_idx = [i for i, m in enumerate(methods) if "FauxPy" in m]
    for i in fauxpy_idx:
        ax.axvspan(i - 0.4, i + 0.4, color="#E07B39", alpha=0.07, zorder=0)

    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=30, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("F1 Score")
    ax.set_title("Minimal Set F1 by Injected-Bug Category (Bench)")
    ax.legend(fontsize=9, ncol=4, loc="upper right")
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure2_bench_minimal_set_by_category.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()