"""
Table 1. Headline solve rate by (repair type x model), on the comparable
4-question basis (question 2 excluded so every model is judged on the same
1,348 submissions).
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

from common import (
    OUT_TABLES, OUT_FIGURES, MODELS, TYPES, MODEL_LABELS, TYPE_LABELS,
    load_records, comparable,
)


def build_table1() -> pd.DataFrame:
    df = comparable(load_records())
    pivot = df.groupby(["repair_model", "repair_type"])["solved"].mean().unstack()
    pivot = pivot.reindex(index=MODELS, columns=TYPES)
    pivot.index = [MODEL_LABELS[m] for m in pivot.index]
    pivot.columns = [TYPE_LABELS[t] for t in pivot.columns]
    return pivot


def main():
    table1 = build_table1().round(3)
    print("Solve rate by repair type x model (questions 1,3,4,5; n=1348 per cell)\n")
    print(table1.to_string())
    table1.to_csv(OUT_TABLES / "table1_solve_rate.csv")
    print(f"\n[saved] {OUT_TABLES / 'table1_solve_rate.csv'}")

    methods = list(table1.index)
    x = np.arange(len(methods))
    width = 0.2
    colors = {"None": "#8B8378", "FauxPy": "#E07B39", "Best-Loc (Gemma4)": "#4878CF", "Self-LLM": "#6ACC65"}

    fig, ax = plt.subplots(figsize=(13, 5.5))
    for i, col in enumerate(table1.columns):
        ax.bar(x + (i - 1.5) * width, table1[col].tolist(), width, label=col, color=colors[col], alpha=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=20, ha="right", fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("Solve rate")
    ax.set_title("Repair Solve Rate by Type and Model (Refactory, questions 1,3,4,5)")
    ax.legend(fontsize=9, ncol=4, loc="upper right")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure1_solve_rate.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()