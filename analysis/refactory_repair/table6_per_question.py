"""
Table 6. Per-question solve rate, using ONLY the 4 models with fully
complete data across all 5 questions (Qwen2.5, Qwen3.6, Qwen3Coder,
CodeGemma) -- this isolates question difficulty from the data-completeness
gaps affecting the other 4 models, and quantifies why question 2 was later
dropped from new runs ("almost always failing after 4 tries").
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

from common import (
    OUT_TABLES, OUT_FIGURES, FULLY_COMPLETE_MODELS, MODEL_LABELS, QUESTIONS,
    load_records,
)


def build_table6() -> pd.DataFrame:
    df = load_records()
    sub = df[df["repair_model"].isin(FULLY_COMPLETE_MODELS)]
    pivot = sub.groupby(["question", "repair_type"])["solved"].mean().unstack()
    n = sub.groupby(["question", "repair_type"]).size().unstack()
    return pivot, n


def main():
    table6, n = build_table6()
    table6 = table6.round(3)
    print("Solve rate by question, pooled across the 4 fully-complete models")
    print("(Qwen2.5, Qwen3.6, Qwen3Coder, CodeGemma)\n")
    print(table6.to_string())
    print("\nn per cell:")
    print(n.to_string())
    table6.to_csv(OUT_TABLES / "table6_per_question.csv")
    print(f"\n[saved] {OUT_TABLES / 'table6_per_question.csv'}")

    fig, ax = plt.subplots(figsize=(9, 5.5))
    colors = {"none": "#8B8378", "fauxpy": "#E07B39", "best_loc": "#4878CF", "self_llm": "#6ACC65"}
    for t in table6.columns:
        ax.plot(table6.index, table6[t], marker="o", label=t, color=colors.get(t, None), linewidth=2)
    ax.axvspan(1.6, 2.4, color="#D65F5F", alpha=0.1, zorder=0)
    ax.text(2, 0.05, "Question 2", ha="center", fontsize=9, color="#D65F5F")
    ax.set_xticks(QUESTIONS)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_xlabel("Question")
    ax.set_ylabel("Solve rate")
    ax.set_title("Solve Rate by Question (4 fully-complete models pooled)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure6_per_question.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()