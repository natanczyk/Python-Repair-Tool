"""
Ranking agreement on QuixBugs -- direct parallel to table2_ranking_agreement.py
(Refactory).

For each LLM, compares its full line ranking to FauxPy's (SBFL) ranking on the
same program, restricted to the lines both methods actually rank. Spearman
rho and Kendall tau are computed per program on that common subset, then
averaged across all programs where at least 2 lines overlap.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import spearmanr, kendalltau

from common import MODELS, MODEL_LABELS, OUT_TABLES, load_ranking


def rank_agreement(ranked_a: list[int], ranked_b: list[int]) -> tuple[float, float] | None:
    common = [l for l in ranked_a if l in ranked_b]
    if len(common) < 2:
        return None
    rank_a = {l: i for i, l in enumerate(ranked_a)}
    rank_b = {l: i for i, l in enumerate(ranked_b)}
    a = [rank_a[l] for l in common]
    b = [rank_b[l] for l in common]
    rho, _ = spearmanr(a, b)
    tau, _ = kendalltau(a, b)
    return float(rho), float(tau)


def build_table2() -> tuple[list[str], list[float], list[float], list[int]]:
    fauxpy_ranking = load_ranking("fauxpy")

    methods, spearman_vals, kendall_vals, n_vals = [], [], [], []
    for m in MODELS:
        llm_ranking = load_ranking(m)
        common_progs = [p for p in fauxpy_ranking if p in llm_ranking]

        rhos, taus = [], []
        for prog in common_progs:
            result = rank_agreement(fauxpy_ranking[prog], llm_ranking[prog])
            if result is None:
                continue
            rho, tau = result
            if not np.isnan(rho):
                rhos.append(rho)
            if not np.isnan(tau):
                taus.append(tau)

        methods.append(MODEL_LABELS[m])
        spearman_vals.append(np.mean(rhos) if rhos else float("nan"))
        kendall_vals.append(np.mean(taus) if taus else float("nan"))
        n_vals.append(len(rhos))

    return methods, spearman_vals, kendall_vals, n_vals


if __name__ == "__main__":
    methods, spearman_vals, kendall_vals, n_vals = build_table2()

    print("Ranking agreement: LLM ranking vs FauxPy (SBFL) ranking, restricted")
    print("to lines both methods rank in a given program (QuixBugs, questions 1-40)\n")

    header = f"{'Model':<20}{'Spearman':>10}{'Kendall tau':>14}{'n':>8}"
    print(header)
    print("-" * len(header))
    for method, rho, tau, n in zip(methods, spearman_vals, kendall_vals, n_vals):
        print(f"{method:<20}{rho:>10.3f}{tau:>14.3f}{n:>8}")

    csv_path = OUT_TABLES / "table2_ranking_agreement.csv"
    with csv_path.open("w", encoding="utf-8") as f:
        f.write("Model,Spearman,Kendall_tau,n\n")
        for method, rho, tau, n in zip(methods, spearman_vals, kendall_vals, n_vals):
            f.write(f"{method},{rho:.4f},{tau:.4f},{n}\n")
    print(f"\n[saved] {csv_path}")