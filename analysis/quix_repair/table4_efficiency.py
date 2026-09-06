"""
Efficiency on QuixBugs: among SOLVED submissions only, how many iterations
did it take? -- direct parallel to table4_efficiency.py (Refactory). Solve
rate alone conflates "solves fast" with "barely scrapes by".
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from common import (
    OUT_TABLES, OUT_FIGURES, MODELS, TYPES, MODEL_LABELS, TYPE_LABELS,
    load_records, comparable,
)


def build_table4() -> pd.DataFrame:
    df = comparable(load_records())
    solved = df[df["solved"]]
    pivot = solved.groupby(["repair_model", "repair_type"])["iterations"].mean().unstack()
    pivot = pivot.reindex(index=MODELS, columns=TYPES)
    pivot.index = [MODEL_LABELS[m] for m in pivot.index]
    pivot.columns = [TYPE_LABELS[t] for t in pivot.columns]
    return pivot


def main():
    table4 = build_table4().round(3)
    print("Mean iterations to solve (solved cases only; QuixBugs, questions 1-40)\n")
    print(table4.to_string())
    table4.to_csv(OUT_TABLES / "table4_efficiency.csv")
    print(f"\n[saved] {OUT_TABLES / 'table4_efficiency.csv'}")

    methods = list(table4.index)
    x = np.arange(len(methods))
    width = 0.2
    colors = {"None": "#8B8378", "FauxPy": "#E07B39", "Best-Loc (Gemma4)": "#4878CF", "Self-LLM": "#6ACC65"}

    fig, ax = plt.subplots(figsize=(13, 5.5))
    for i, col in enumerate(table4.columns):
        ax.bar(x + (i - 1.5) * width, table4[col].tolist(), width, label=col, color=colors[col], alpha=0.9)
    ax.set_xticks(x)
    ax.set_xticklabels(methods, rotation=20, ha="right", fontsize=9)
    ax.set_ylabel("Mean iterations to solve")
    ax.set_title("Repair Efficiency by Type and Model (QuixBugs, solved cases only)")
    ax.legend(fontsize=9, ncol=4, loc="upper left")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure4_efficiency.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()