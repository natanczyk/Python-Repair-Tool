"""
Study 1 - Fault Localization
Figures for Table 1 (Overall localization performance).

Two grouped bar charts, no heatmaps:
  Figure 1 - Ranking quality: Top-1, Top-3, Top-6, MRR per method.
  Figure 2 - Minimal Set Precision / Recall / F1 per method.

FauxPy is drawn in a distinct color/hatch since it is the non-LLM baseline.
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
LLM_COLOR    = "#4878CF"


def method_colors(methods: list[str]) -> list[str]:
    return [FAUXPY_COLOR if "FauxPy" in m else LLM_COLOR for m in methods]


def method_hatches(methods: list[str]) -> list[str]:
    return ["//" if "FauxPy" in m else "" for m in methods]


def grouped_bar(ax, methods, series: dict[str, list[float]], colors_by_series: dict[str, str]):
    x = np.arange(len(methods))
    n = len(series)
    width = 0.8 / n
    for i, (label, vals) in enumerate(series.items()):
        offset = (i - (n - 1) / 2) * width
        bars = ax.bar(x + offset, vals, width, label=label,
                       color=colors_by_series[label], alpha=0.88)
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=30, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.grid(axis="y", alpha=0.3)


def main():
    table1 = build_table1().round(3)
    methods = list(table1.index)

    # ── Figure 1: Top-1 / Top-3 / Top-6 / MRR ────────────────────────────────
    fig, ax = plt.subplots(figsize=(13, 5.5))
    series = {
        "Top-1": table1["Top-1"].tolist(),
        "Top-3": table1["Top-3"].tolist(),
        "Top-6": table1["Top-6"].tolist(),
        "MRR": table1["MRR"].tolist(),
    }
    colors_by_series = {
        "Top-1": "#4878CF", "Top-3": "#6ACC65", "Top-6": "#D65F5F", "MRR": "#8064A2",
    }
    grouped_bar(ax, methods, series, colors_by_series)
    ax.set_ylabel("Score")
    ax.set_title("Ranking Quality: Top-1 / Top-3 / Top-6 / MRR (Refactory Dataset)")
    ax.legend(fontsize=9, ncol=4, loc="upper left")

    # Visually flag the FauxPy baseline column with a light background band
    fauxpy_idx = [i for i, m in enumerate(methods) if "FauxPy" in m]
    for i in fauxpy_idx:
        ax.axvspan(i - 0.4, i + 0.4, color=FAUXPY_COLOR, alpha=0.07, zorder=0)

    plt.tight_layout()
    fig1_path = OUT_DIR / "table1_fig1_ranking_quality.png"
    plt.savefig(fig1_path, dpi=150)
    plt.close()

    # ── Figure 2: Minimal Set F1 ─────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(13, 5.5))
    colors = method_colors(methods)
    bars = ax.bar(methods, table1["Minimal Set F1"].tolist(), color=colors, alpha=0.88)
    for bar, v in zip(bars, table1["Minimal Set F1"].tolist()):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f"{v:.3f}", ha="center", va="bottom", fontsize=9)
    ax.set_xticks(range(len(methods)))
    ax.set_xticklabels(methods, rotation=30, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.grid(axis="y", alpha=0.3)
    ax.set_ylabel("F1 Score")
    ax.set_title("Minimal Bug Set Recovery: F1 (top lines matching GT quantity, Refactory Dataset)")

    for i in fauxpy_idx:
        ax.axvspan(i - 0.4, i + 0.4, color=FAUXPY_COLOR, alpha=0.07, zorder=0)

    plt.tight_layout()
    fig2_path = OUT_DIR / "table1_fig2_minimal_set_prf.png"
    plt.savefig(fig2_path, dpi=150)
    plt.close()

    print(f"[saved] {fig1_path}")
    print(f"[saved] {fig2_path}")


if __name__ == "__main__":
    main()
