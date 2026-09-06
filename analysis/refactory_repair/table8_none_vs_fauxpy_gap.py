"""
Table 8. Does FauxPy (SBFL) localization guidance improve repair over blind
(`none`) repair, holding the repair model fixed?

Companion figure to table3_localizer_quality_gap.png (best_loc vs self_llm),
but for none vs fauxpy -- isolates the effect of adding SBFL suspicious-line
guidance to an otherwise identical repair loop and prompt. Table 2's McNemar
test already reports this pairing in text form; this adds the solve-rate gap
and a figure in the same visual style as Table 3.
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
from scipy.stats import binomtest

from common import OUT_TABLES, OUT_FIGURES, MODELS, MODEL_LABELS, load_records, comparable


def build_table8() -> pd.DataFrame:
    df = comparable(load_records())
    rows = []
    for model in MODELS:
        sub = df[df["repair_model"] == model]
        wide = sub.pivot(index="submission", columns="repair_type", values="solved")
        wide = wide.dropna(subset=["none", "fauxpy"])
        fauxpy_only = int(((wide["fauxpy"]) & (~wide["none"])).sum())
        none_only = int(((~wide["fauxpy"]) & (wide["none"])).sum())
        n_disc = fauxpy_only + none_only
        p = binomtest(fauxpy_only, n_disc, 0.5, alternative="two-sided").pvalue if n_disc else 1.0
        rows.append({
            "Model": MODEL_LABELS[model],
            "None rate": wide["none"].mean(),
            "FauxPy rate": wide["fauxpy"].mean(),
            "Gap (FauxPy - None)": wide["fauxpy"].mean() - wide["none"].mean(),
            "p-value": p,
        })
    return pd.DataFrame(rows).set_index("Model")


def main():
    table8 = build_table8()
    print("FauxPy-guided vs blind (`none`) repair, per repair model\n")
    print(table8.round(4).to_string())
    table8.round(4).to_csv(OUT_TABLES / "table8_none_vs_fauxpy_gap.csv")
    print(f"\n[saved] {OUT_TABLES / 'table8_none_vs_fauxpy_gap.csv'}")

    methods = list(table8.index)
    gap = table8["Gap (FauxPy - None)"].tolist()
    pvals = table8["p-value"].tolist()
    colors = [
        "#6ACC65" if (g > 0 and p < 0.05) else
        "#D65F5F" if (g < 0 and p < 0.05) else
        "#B0B0B0"
        for g, p in zip(gap, pvals)
    ]

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
    ax.set_ylabel("Solve rate gap: FauxPy - None")
    ax.set_title("Effect of Adding FauxPy (SBFL) Localization vs Blind Repair")
    ax.grid(axis="y", alpha=0.3)

    from matplotlib.patches import Patch
    ax.legend(handles=[
        Patch(color="#6ACC65", label="FauxPy significantly better (p<0.05)"),
        Patch(color="#D65F5F", label="FauxPy significantly worse (p<0.05)"),
        Patch(color="#B0B0B0", label="Not statistically significant"),
    ], fontsize=8.5, loc="upper right")

    plt.tight_layout()
    fig_path = OUT_FIGURES / "figure8_none_vs_fauxpy_gap.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()
    print(f"[saved] {fig_path}")


if __name__ == "__main__":
    main()