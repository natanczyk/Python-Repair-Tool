"""
Study 1 - Fault Localization
Figure for Table 2 (Ranking agreement).

Grouped bar chart, no heatmap: Spearman rho and Kendall tau per LLM,
measuring agreement with the FauxPy (SBFL) ranking.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from table2_ranking_agreement import build_table2

OUT_DIR = Path(__file__).parent / "figures"
OUT_DIR.mkdir(exist_ok=True)


def main():
    methods, spearman_vals, kendall_vals, _ = build_table2()

    x = np.arange(len(methods))
    width = 0.35

    fig, ax = plt.subplots(figsize=(11, 5.5))
    bars_s = ax.bar(x - width / 2, spearman_vals, width, label="Spearman ρ", color="#4878CF", alpha=0.88)
    bars_k = ax.bar(x + width / 2, kendall_vals, width, label="Kendall τ", color="#D65F5F", alpha=0.88)

    for bars in (bars_s, bars_k):
        for bar in bars:
            v = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, v + (0.005 if v >= 0 else -0.015),
                    f"{v:.3f}", ha="center", va="bottom" if v >= 0 else "top", fontsize=8)

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=30, ha="right", fontsize=9)
    ax.set_ylabel("Correlation with FauxPy (SBFL) ranking")
    ax.set_title("Ranking Agreement: LLM vs FauxPy (SBFL) (Refactory)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    fig_path = OUT_DIR / "table2_fig3_ranking_agreement.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()
