"""
Per-question solve rate on QuixBugs -- direct parallel to
table6_per_question.py (Refactory). Unlike Refactory (which restricts to
the 4 fully-complete models to isolate question difficulty from
data-completeness gaps), QuixBugs data is essentially complete across all
8 models, so all 8 are pooled directly. Also unlike Refactory, there's no
single known-bad question to flag -- QuixBugs' hard cases (genuine infinite
loops / intractable recursion) are spread across several different
questions rather than concentrated in one, so no special highlighting is
applied here; low points in the line chart are the signal.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

from common import OUT_TABLES, OUT_FIGURES, MODELS, MODEL_LABELS, QUESTIONS, load_records


def build_table6() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = load_records()
    pivot = df.groupby(["question", "repair_type"])["solved"].mean().unstack()
    n = df.groupby(["question", "repair_type"]).size().unstack()
    return pivot, n


def main():
    table6, n = build_table6()
    table6 = table6.round(3)
    print("Solve rate by question, pooled across all 8 models (QuixBugs)\n")
    print(table6.to_string())
    print("\nn per cell:")
    print(n.to_string())
    table6.to_csv(OUT_TABLES / "table6_per_question.csv")
    print(f"\n[saved] {OUT_TABLES / 'table6_per_question.csv'}")

    fig, ax = plt.subplots(figsize=(14, 5.5))
    colors = {"none": "#8B8378", "fauxpy": "#E07B39", "best_loc": "#4878CF", "self_llm": "#6ACC65"}
    for t in table6.columns:
        ax.plot(table6.index, table6[t], marker="o", label=t, color=colors.get(t, None), linewidth=1.5, markersize=4)
    ax.set_xticks(QUESTIONS)
    ax.set_xticklabels(QUESTIONS, fontsize=7, rotation=90)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_xlabel("Question")
    ax.set_ylabel("Solve rate")
    ax.set_title("Solve Rate by Question (QuixBugs, all 8 models pooled)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure6_per_question.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()