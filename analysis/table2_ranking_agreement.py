"""
Study 1 - Fault Localization
Table 2. Ranking agreement

For each LLM, compares its full line ranking to FauxPy's (SBFL) ranking on the
same submission, restricted to the lines both methods actually rank (FauxPy
does not always rank every line in a file). Spearman rho and Kendall tau are
computed per submission on that common subset, then averaged across all
submissions where at least 2 lines overlap.

Answers: how similar are LLM rankings to SBFL rankings?
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr, kendalltau

ROOT      = Path(__file__).parent.parent
REF_LOC   = ROOT / "results_v2" / "refactory_loc"
OUT_DIR   = Path(__file__).parent / "tables"
OUT_DIR.mkdir(exist_ok=True)

QUESTIONS = [1, 2, 3, 4, 5]

MODELS = [
    "qwen", "qwen3_27b", "qwen3_coder", "gemma4",
    "granite4", "codegemma", "granite_code", "codellama",
]

MODEL_LABELS = {
    "qwen":         "Qwen2.5",
    "qwen3_27b":    "Qwen3.6",
    "qwen3_coder":  "Qwen3Coder",
    "gemma4":       "Gemma4",
    "granite4":     "Granite4",
    "codegemma":    "CodeGemma",
    "granite_code": "GraniteCode",
    "codellama":    "CodeLlama",
}


def load_jsonl(path: Path) -> dict[str, list[int]]:
    if not path.exists():
        return {}
    data = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            data[r["program_name"]] = r["buggy_lines"]
    return data


def load_ranking(method: str) -> dict[str, list[int]]:
    fname = "fauxpy_localization.jsonl" if method == "fauxpy" else f"llm_{method}_localization.jsonl"
    preds = {}
    for q in QUESTIONS:
        preds.update(load_jsonl(REF_LOC / f"question_{q}" / fname))
    return preds


def rank_agreement(ranked_a: list[int], ranked_b: list[int]) -> tuple[float, float] | None:
    """Spearman rho and Kendall tau on lines common to both rankings.
    Returns None if fewer than 2 lines overlap."""
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
    print("to lines both methods rank in a given submission (Refactory, questions 1-5)\n")

    header = f"{'Model':<20}{'Spearman':>10}{'Kendall tau':>14}{'n':>8}"
    print(header)
    print("-" * len(header))
    for method, rho, tau, n in zip(methods, spearman_vals, kendall_vals, n_vals):
        print(f"{method:<20}{rho:>10.3f}{tau:>14.3f}{n:>8}")

    csv_path = OUT_DIR / "table2_ranking_agreement.csv"
    with csv_path.open("w", encoding="utf-8") as f:
        f.write("Model,Spearman,Kendall_tau,n\n")
        for method, rho, tau, n in zip(methods, spearman_vals, kendall_vals, n_vals):
            f.write(f"{method},{rho:.4f},{tau:.4f},{n}\n")
    print(f"\n[saved] {csv_path}")
