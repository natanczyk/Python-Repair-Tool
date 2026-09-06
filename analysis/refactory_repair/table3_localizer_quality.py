"""
Table 3. Does the localizer's quality matter, holding the repair model fixed?

best_loc always uses Gemma4 (a strong standalone localizer) regardless of
repair model; self_llm uses the repair model's own localization. Comparing
best_loc vs self_llm per model isolates localization quality from repair
quality. Cross-referenced against ANCHORING_MODELS (granite_code, codegemma,
qwen), which showed prompt-anchoring bias in standalone localization
(Table 1 of the localization chapter).
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from scipy.stats import binomtest

from common import (
    OUT_TABLES, OUT_FIGURES, MODELS, MODEL_LABELS, ANCHORING_MODELS,
    load_records, comparable,
)


def build_table3() -> pd.DataFrame:
    df = comparable(load_records())
    rows = []
    for model in MODELS:
        sub = df[df["repair_model"] == model]
        wide = sub.pivot(index="submission", columns="repair_type", values="solved")
        wide = wide.dropna(subset=["best_loc", "self_llm"])
        best_loc_only = int(((wide["best_loc"]) & (~wide["self_llm"])).sum())
        self_llm_only = int(((~wide["best_loc"]) & (wide["self_llm"])).sum())
        n_disc = best_loc_only + self_llm_only
        p = binomtest(best_loc_only, n_disc, 0.5, alternative="two-sided").pvalue if n_disc else 1.0
        rows.append({
            "Model": MODEL_LABELS[model],
            "Anchoring-biased?": "yes" if model in ANCHORING_MODELS else "no",
            "Best-Loc rate": wide["best_loc"].mean(),
            "Self-LLM rate": wide["self_llm"].mean(),
            "Gap (Best-Loc - Self-LLM)": wide["best_loc"].mean() - wide["self_llm"].mean(),
            "p-value": p,
        })
    return pd.DataFrame(rows).set_index("Model")


def main():
    table3 = build_table3()
    print("Best-Loc (Gemma4 localizer) vs Self-LLM (own localization), per repair model\n")
    print(table3.round(4).to_string())
    table3.round(4).to_csv(OUT_TABLES / "table3_localizer_quality.csv")
    print(f"\n[saved] {OUT_TABLES / 'table3_localizer_quality.csv'}")

    methods = list(table3.index)
    gap = table3["Gap (Best-Loc - Self-LLM)"].tolist()
    colors = ["#D65F5F" if a == "yes" else "#4878CF" for a in table3["Anchoring-biased?"]]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    bars = ax.bar(methods, gap, color=colors, alpha=0.9)
    for bar, v in zip(bars, gap):
        ax.text(bar.get_x() + bar.get_width() / 2, v + (0.01 if v >= 0 else -0.02),
                f"{v:+.3f}", ha="center", va="bottom" if v >= 0 else "top", fontsize=9)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_ylim(min(gap) - 0.03, max(gap) + 0.08)
    ax.set_xticks(range(len(methods)))
    ax.set_xticklabels(methods, rotation=20, ha="right", fontsize=9)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_ylabel("Solve rate gap: Best-Loc - Self-LLM")
    ax.set_title("Effect of Swapping in a Stronger Localizer (Gemma4) vs Self-Localization")
    ax.grid(axis="y", alpha=0.3)

    from matplotlib.patches import Patch
    ax.legend(handles=[
        Patch(color="#D65F5F", label="Anchoring-biased"),
        Patch(color="#4878CF", label="Not anchoring-biased"),
    ], fontsize=8.5, loc="upper right")

    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure3_localizer_quality_gap.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()