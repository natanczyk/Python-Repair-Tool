"""
Figure for Table 5: Minimal set F1 with test feedback vs. without test
feedback, per LLM. Grouped bar chart, no heatmap. FauxPy (top-|GT|) is
drawn as a reference line, matching Table 3's baseline.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

from table5_minimal_set_tests_vs_notests import build_table5
from table3_minimal_set_llm import compute_fauxpy_metrics, load_ground_truth

OUT_DIR = Path(__file__).parent / "figures"
OUT_DIR.mkdir(exist_ok=True)

FAUXPY_COLOR = "#E07B39"


def main():
    table5 = build_table5().round(3)
    methods = list(table5.index)

    gt = load_ground_truth()
    fauxpy_f1 = compute_fauxpy_metrics(gt)["F1"]

    x = np.arange(len(methods))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 5.5))
    bars_t  = ax.bar(x - width / 2, table5["F1 (with tests)"].tolist(), width,
                      label="With tests", color="#4878CF", alpha=0.88)
    bars_nt = ax.bar(x + width / 2, table5["F1 (without tests)"].tolist(), width,
                      label="Without tests", color="#D65F5F", alpha=0.88)

    for bars in (bars_t, bars_nt):
        for bar in bars:
            v = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, v + 0.01,
                    f"{v:.3f}", ha="center", va="bottom", fontsize=7.5)

    

    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=25, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("Minimal Set F1")
    ax.set_title("Minimal Set Detection: With Tests vs. Without Tests (Refactory)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig_path = OUT_DIR / "figure5_minimal_set_tests_vs_notests.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()
