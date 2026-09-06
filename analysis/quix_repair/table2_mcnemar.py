"""
Paired significance testing (McNemar's exact test) on QuixBugs -- direct
parallel to table2_mcnemar.py (Refactory). Does localization guidance
actually improve repair over blind (`none`) repair?

For each model, compares `none` vs each of `fauxpy`/`best_loc`/`self_llm` on
the *same* submissions (paired), using the exact binomial form of McNemar's
test on the discordant pairs.
"""
from __future__ import annotations

import pandas as pd
from scipy.stats import binomtest

from common import OUT_TABLES, MODELS, MODEL_LABELS, load_records, comparable


def mcnemar(a_solved: pd.Series, b_solved: pd.Series) -> tuple[int, int, float]:
    """Returns (a_only, b_only, two-sided exact p-value) where a_only = A solved & B failed,
    b_only = A failed & B solved."""
    a_only = int(((a_solved) & (~b_solved)).sum())
    b_only = int(((~a_solved) & (b_solved)).sum())
    n = a_only + b_only
    if n == 0:
        return a_only, b_only, 1.0
    p = binomtest(b_only, n, 0.5, alternative="two-sided").pvalue
    return a_only, b_only, p


def build_table2() -> pd.DataFrame:
    df = comparable(load_records())
    rows = []
    for model in MODELS:
        sub = df[df["repair_model"] == model]
        wide = sub.pivot(index="submission", columns="repair_type", values="solved")
        wide = wide.dropna(subset=["none", "fauxpy", "best_loc", "self_llm"])
        row = {"Model": MODEL_LABELS[model], "n": len(wide)}
        for other in ["fauxpy", "best_loc", "self_llm"]:
            none_only, other_only, p = mcnemar(wide["none"], wide[other])
            direction = "+" if other_only > none_only else ("-" if other_only < none_only else "=")
            sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
            row[f"{other} vs none"] = f"{direction}{abs(other_only - none_only)} (p={p:.1e}, {sig})"
        rows.append(row)
    return pd.DataFrame(rows).set_index("Model")


if __name__ == "__main__":
    table2 = build_table2()
    print("McNemar's exact test: each localization-guided repair type vs `none` (paired, per model)")
    print("Format: <net change in solved count> (p-value, significance) -- QuixBugs, questions 1-40\n")
    print(table2.to_string())
    table2.to_csv(OUT_TABLES / "table2_mcnemar.csv")
    print(f"\n[saved] {OUT_TABLES / 'table2_mcnemar.csv'}")