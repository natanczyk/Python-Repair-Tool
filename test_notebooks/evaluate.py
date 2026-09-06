"""
Evaluation of fault localization results against ground truth.

Comparisons:
  1. Minimal set (LLM no-tests / with-tests) vs ground truth — Precision, Recall, F1
  2. Ranking (FauxPy + LLMs) vs ground truth — Top-K accuracy, MRR
  3. FauxPy ranking vs LLM rankings — Spearman rank correlation, Top-K overlap
  4. Up-to-3 buggy lines vs ground truth — Precision, Recall, F1

Outputs:
  - Console summary tables
  - Visualisations saved to Wyniki/plots/
"""

from __future__ import annotations

import json
from pathlib import Path
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
from scipy.stats import spearmanr

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BASE        = Path(__file__).parent
WYNIKI      = BASE / "Wyniki"
DATA        = BASE / "Data"
PLOTS_DIR   = WYNIKI / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

QUESTIONS   = [1, 2, 3, 4, 5]
RANKING_DIR = WYNIKI / "ranking_buggy_lines"
MIN_NO_TEST = WYNIKI / "minimal_set_llm_no_tests"
MIN_W_TEST  = WYNIKI / "minimal_set_llm_using_tests"
UP_TO_3_DIR = WYNIKI / "Up_to_3_buggy_lines"

LLM_MODELS  = ["qwen", "qwen3_27b", "qwen3_coder", "gemma4"]

# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def load_jsonl(path: Path) -> dict[str, list[int]]:
    """Returns {program_name: buggy_lines}."""
    if not path.exists():
        return {}
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        entry = json.loads(line)
        result[entry["program_name"]] = entry["buggy_lines"]
    return result


def load_ground_truth(question: int) -> dict[str, list[int]]:
    return load_jsonl(DATA / f"question_{question}" / "ground_truth.jsonl")


def load_ranking(question: int, model: str) -> dict[str, list[int]]:
    fname = "fauxpy_localization.jsonl" if model == "fauxpy" else f"llm_{model}_localization.jsonl"
    return load_jsonl(RANKING_DIR / f"question_{question}" / fname)


def load_minimal(question: int, model: str, with_tests: bool) -> dict[str, list[int]]:
    folder = MIN_W_TEST if with_tests else MIN_NO_TEST
    return load_jsonl(folder / f"question_{question}" / f"llm_{model}_minimal_localization.jsonl")


def load_up_to_3(question: int, model: str) -> dict[str, list[int]]:
    return load_jsonl(UP_TO_3_DIR / f"question_{question}" / f"llm_{model}_localization.jsonl")


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def precision_recall_f1(pred: list[int], gt: list[int]) -> tuple[float, float, float]:
    if not pred and not gt:
        return 1.0, 1.0, 1.0
    if not pred or not gt:
        return 0.0, 0.0, 0.0
    pred_set, gt_set = set(pred), set(gt)
    tp = len(pred_set & gt_set)
    p  = tp / len(pred_set)
    r  = tp / len(gt_set)
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return p, r, f1


def top_k_hit(ranked: list[int], gt: list[int], k: int) -> bool:
    """True if at least one gt line appears in top-k of ranked."""
    gt_set = set(gt)
    return any(line in gt_set for line in ranked[:k])


def recall_at_k(ranked: list[int], gt: list[int], k: int) -> float:
    """Fraction of ground truth lines found in top-k (Recall@K)."""
    if not gt:
        return 1.0
    gt_set = set(gt)
    found = sum(1 for line in ranked[:k] if line in gt_set)
    return found / len(gt_set)


def precision_at_k(ranked: list[int], gt: list[int], k: int) -> float:
    """Fraction of top-k predictions that are in ground truth (Precision@K)."""
    top = ranked[:k]
    if not top:
        return 0.0
    gt_set = set(gt)
    return sum(1 for line in top if line in gt_set) / len(top)


def f1_at_k(ranked: list[int], gt: list[int], k: int) -> float:
    p = precision_at_k(ranked, gt, k)
    r = recall_at_k(ranked, gt, k)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def mrr(ranked: list[int], gt: list[int]) -> float:
    """Mean Reciprocal Rank: 1/rank of first correct line, 0 if none found."""
    gt_set = set(gt)
    for i, line in enumerate(ranked, 1):
        if line in gt_set:
            return 1.0 / i
    return 0.0


def spearman_overlap(ranked_a: list[int], ranked_b: list[int]) -> float:
    """Spearman correlation on lines present in both rankings."""
    common = [l for l in ranked_a if l in ranked_b]
    if len(common) < 2:
        return float("nan")
    rank_a = {l: i for i, l in enumerate(ranked_a)}
    rank_b = {l: i for i, l in enumerate(ranked_b)}
    a = [rank_a[l] for l in common]
    b = [rank_b[l] for l in common]
    corr, _ = spearmanr(a, b)
    return float(corr)


# ---------------------------------------------------------------------------
# Aggregation helpers
# ---------------------------------------------------------------------------

def aggregate_prf(question: int, pred_fn) -> dict[str, float]:
    gt_all = load_ground_truth(question)
    ps, rs, fs = [], [], []
    for prog, gt in gt_all.items():
        pred = pred_fn(prog)
        p, r, f = precision_recall_f1(pred, gt)
        ps.append(p); rs.append(r); fs.append(f)
    return {"precision": np.mean(ps), "recall": np.mean(rs), "f1": np.mean(fs), "n": len(ps)}


def aggregate_ranking(question: int, ranked_fn) -> dict[str, float]:
    gt_all = load_ground_truth(question)
    hits1, hits3, hits5, mrrs = [], [], [], []
    for prog, gt in gt_all.items():
        ranked = ranked_fn(prog)
        if not gt:
            continue
        hits1.append(top_k_hit(ranked, gt, 1))
        hits3.append(top_k_hit(ranked, gt, 3))
        hits5.append(top_k_hit(ranked, gt, 5))
        mrrs.append(mrr(ranked, gt))
    return {
        "top1": np.mean(hits1), "top3": np.mean(hits3),
        "top5": np.mean(hits5), "mrr":  np.mean(mrrs),
        "n": len(hits1),
    }


# ---------------------------------------------------------------------------
# Section 1: Minimal set vs ground truth
# ---------------------------------------------------------------------------

def eval_minimal_set():
    print("\n" + "="*70)
    print("1. MINIMAL SET vs GROUND TRUTH")
    print("="*70)

    rows = []
    for variant, with_tests in [("no_tests", False), ("with_tests", True)]:
        for model in LLM_MODELS:
            ps, rs, fs = [], [], []
            for q in QUESTIONS:
                preds = load_minimal(q, model, with_tests)
                gt_all = load_ground_truth(q)
                for prog, gt in gt_all.items():
                    pred = preds.get(prog, [])
                    p, r, f = precision_recall_f1(pred, gt)
                    ps.append(p); rs.append(r); fs.append(f)
            rows.append({
                "variant": variant, "model": model,
                "P": np.mean(ps), "R": np.mean(rs), "F1": np.mean(fs),
            })
            print(f"  [{variant}] {model:15s}  P={np.mean(ps):.3f}  R={np.mean(rs):.3f}  F1={np.mean(fs):.3f}")
    return rows


# ---------------------------------------------------------------------------
# Section 2: Ranking vs ground truth
# ---------------------------------------------------------------------------

def eval_ranking_vs_gt():
    print("\n" + "="*70)
    print("2. RANKING vs GROUND TRUTH (Precision@K, Recall@K, F1@K, MRR)")
    print("="*70)

    rows = []
    all_models = ["fauxpy"] + LLM_MODELS
    for model in all_models:
        p1s, p3s, p5s = [], [], []
        r1s, r3s, r5s = [], [], []
        f1s, f3s, f5s = [], [], []
        mrrs = []
        for q in QUESTIONS:
            preds = load_ranking(q, model)
            gt_all = load_ground_truth(q)
            for prog, gt in gt_all.items():
                ranked = preds.get(prog, [])
                if not gt:
                    continue
                p1s.append(precision_at_k(ranked, gt, 1))
                p3s.append(precision_at_k(ranked, gt, 3))
                p5s.append(precision_at_k(ranked, gt, 5))
                r1s.append(recall_at_k(ranked, gt, 1))
                r3s.append(recall_at_k(ranked, gt, 3))
                r5s.append(recall_at_k(ranked, gt, 5))
                f1s.append(f1_at_k(ranked, gt, 1))
                f3s.append(f1_at_k(ranked, gt, 3))
                f5s.append(f1_at_k(ranked, gt, 5))
                mrrs.append(mrr(ranked, gt))
        rows.append({
            "model": model,
            "p1": np.mean(p1s), "p3": np.mean(p3s), "p5": np.mean(p5s),
            "r1": np.mean(r1s), "r3": np.mean(r3s), "r5": np.mean(r5s),
            "f1": np.mean(f1s), "f3": np.mean(f3s), "f5": np.mean(f5s),
            "mrr": np.mean(mrrs),
        })
        print(f"  {model:15s}  P@1={np.mean(p1s):.3f}  P@3={np.mean(p3s):.3f}  P@5={np.mean(p5s):.3f}  MRR={np.mean(mrrs):.3f}")
        print(f"  {'':15s}  R@1={np.mean(r1s):.3f}  R@3={np.mean(r3s):.3f}  R@5={np.mean(r5s):.3f}")
        print(f"  {'':15s}  F1@1={np.mean(f1s):.3f} F1@3={np.mean(f3s):.3f} F1@5={np.mean(f5s):.3f}")
    return rows


# ---------------------------------------------------------------------------
# Section 3: FauxPy ranking vs LLM rankings
# ---------------------------------------------------------------------------

def eval_fauxpy_vs_llm():
    print("\n" + "="*70)
    print("3. FAUXPY RANKING vs LLM RANKINGS (Spearman correlation)")
    print("="*70)

    rows = []
    for model in LLM_MODELS:
        corrs = []
        for q in QUESTIONS:
            fauxpy_preds = load_ranking(q, "fauxpy")
            llm_preds    = load_ranking(q, model)
            for prog in fauxpy_preds:
                if prog not in llm_preds:
                    continue
                c = spearman_overlap(fauxpy_preds[prog], llm_preds[prog])
                if not np.isnan(c):
                    corrs.append(c)
        mean_c = np.mean(corrs) if corrs else float("nan")
        rows.append({"model": model, "spearman": mean_c})
        print(f"  fauxpy vs {model:15s}  Spearman={mean_c:.3f}")
    return rows


# ---------------------------------------------------------------------------
# Section 4: Up-to-3 vs ground truth
# ---------------------------------------------------------------------------

def eval_up_to_3():
    print("\n" + "="*70)
    print("4. UP-TO-3 BUGGY LINES vs GROUND TRUTH")
    print("="*70)

    rows = []
    available = {"qwen3_27b", "qwen3_coder", "gemma4"}
    for model in LLM_MODELS:
        if model not in available:
            continue
        ps, rs, fs = [], [], []
        for q in QUESTIONS:
            preds = load_up_to_3(q, model)
            gt_all = load_ground_truth(q)
            for prog, gt in gt_all.items():
                pred = preds.get(prog, [])
                p, r, f = precision_recall_f1(pred, gt)
                ps.append(p); rs.append(r); fs.append(f)
        rows.append({"model": model, "P": np.mean(ps), "R": np.mean(rs), "F1": np.mean(fs)})
        print(f"  {model:15s}  P={np.mean(ps):.3f}  R={np.mean(rs):.3f}  F1={np.mean(fs):.3f}")
    return rows


# ---------------------------------------------------------------------------
# Visualisations
# ---------------------------------------------------------------------------

def plot_minimal_set(rows):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Minimal Set vs Ground Truth", fontsize=14)

    for ax, metric in zip(axes, ["P", "R", "F1"]):
        for variant, ls in [("no_tests", "--"), ("with_tests", "-")]:
            vals  = [r[metric] for r in rows if r["variant"] == variant]
            models = [r["model"] for r in rows if r["variant"] == variant]
            ax.bar(
                [m + ("\n(no tests)" if variant == "no_tests" else "\n(w/ tests)") for m in models],
                vals, alpha=0.75, label=variant
            )
        ax.set_title(metric)
        ax.set_ylim(0, 1)
        ax.tick_params(axis="x", labelsize=8)
    axes[0].legend()
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "minimal_set_vs_gt.png", dpi=150)
    plt.close()
    print(f"\n  Saved: {PLOTS_DIR / 'minimal_set_vs_gt.png'}")


def plot_ranking_vs_gt(rows):
    models = [r["model"] for r in rows]
    x = np.arange(len(models))
    width = 0.25

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("Ranking vs Ground Truth", fontsize=14)

    for ax, (prefix, label) in zip(axes, [("p", "Precision@K"), ("r", "Recall@K"), ("f", "F1@K")]):
        all_vals = []
        bars_per_k = []
        for i, k in enumerate([1, 3, 5]):
            vals = [r[f"{prefix}{k}"] for r in rows]
            all_vals.extend(vals)
            bars = ax.bar(x + i * width, vals, width, label=f"@{k}")
            bars_per_k.append((bars, vals))

        # zoom y-axis to data range with padding
        lo = max(0.0, min(all_vals) - 0.08)
        hi = min(1.0, max(all_vals) + 0.10)
        ax.set_ylim(lo, hi)

        # value labels on each bar
        for bars, vals in bars_per_k:
            for bar, v in zip(bars, vals):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + (hi - lo) * 0.01,
                    f"{v:.2f}",
                    ha="center", va="bottom", fontsize=7, rotation=90,
                )

        ax.set_xticks(x + width)
        ax.set_xticklabels(models, rotation=20, ha="right")
        ax.set_title(label)
        ax.yaxis.grid(True, linestyle="--", alpha=0.5)
        ax.set_axisbelow(True)
        ax.legend()

    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "ranking_vs_gt.png", dpi=150)
    plt.close()
    print(f"  Saved: {PLOTS_DIR / 'ranking_vs_gt.png'}")


def plot_spearman(rows):
    models = [r["model"] for r in rows]
    vals   = [r["spearman"] for r in rows]

    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(models, vals, color="steelblue")
    ax.set_ylim(-1, 1)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("FauxPy vs LLM Ranking — Spearman Correlation")
    ax.set_ylabel("Spearman ρ")
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.02, f"{v:.2f}", ha="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "fauxpy_vs_llm_spearman.png", dpi=150)
    plt.close()
    print(f"  Saved: {PLOTS_DIR / 'fauxpy_vs_llm_spearman.png'}")


def plot_top_k_per_question(rows_ranking):
    """Top-1 accuracy per question for each model."""
    all_models = ["fauxpy"] + LLM_MODELS
    fig, ax = plt.subplots(figsize=(12, 5))
    x = np.arange(len(QUESTIONS))
    width = 0.15

    for i, model in enumerate(all_models):
        vals = []
        for q in QUESTIONS:
            preds  = load_ranking(q, model)
            gt_all = load_ground_truth(q)
            hits = []
            for prog, gt in gt_all.items():
                ranked = preds.get(prog, [])
                if gt:
                    hits.append(top_k_hit(ranked, gt, 1))
            vals.append(np.mean(hits) if hits else 0)
        ax.bar(x + i * width, vals, width, label=model)

    ax.set_xticks(x + width * (len(all_models) - 1) / 2)
    ax.set_xticklabels([f"Q{q}" for q in QUESTIONS])
    ax.set_ylim(0, 1)
    ax.set_title("Top-1 Accuracy per Question")
    ax.set_ylabel("Top-1 Hit Rate")
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "top1_per_question.png", dpi=150)
    plt.close()
    print(f"  Saved: {PLOTS_DIR / 'top1_per_question.png'}")


def plot_f1_minimal_comparison(min_rows, up3_rows):
    """Compare F1 of minimal set (no tests, with tests) vs up-to-3."""
    models_min = list({r["model"] for r in min_rows})
    x = np.arange(len(models_min))
    width = 0.25

    fig, ax = plt.subplots(figsize=(10, 5))
    f1_no  = [next((r["F1"] for r in min_rows if r["model"] == m and r["variant"] == "no_tests"), 0) for m in models_min]
    f1_wt  = [next((r["F1"] for r in min_rows if r["model"] == m and r["variant"] == "with_tests"), 0) for m in models_min]
    f1_u3  = [next((r["F1"] for r in up3_rows  if r["model"] == m), 0) for m in models_min]

    ax.bar(x - width, f1_no, width, label="Minimal (no tests)")
    ax.bar(x,         f1_wt, width, label="Minimal (with tests)")
    ax.bar(x + width, f1_u3, width, label="Up-to-3")

    ax.set_xticks(x)
    ax.set_xticklabels(models_min, rotation=15)
    ax.set_ylim(0, 1)
    ax.set_title("F1 Comparison: Minimal Set vs Up-to-3")
    ax.set_ylabel("F1 Score")
    ax.legend()
    plt.tight_layout()
    plt.savefig(PLOTS_DIR / "f1_comparison.png", dpi=150)
    plt.close()
    print(f"  Saved: {PLOTS_DIR / 'f1_comparison.png'}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    min_rows     = eval_minimal_set()
    ranking_rows = eval_ranking_vs_gt()
    spearman_rows = eval_fauxpy_vs_llm()
    up3_rows     = eval_up_to_3()

    print("\n" + "="*70)
    print("GENERATING PLOTS ...")
    plot_minimal_set(min_rows)
    plot_ranking_vs_gt(ranking_rows)
    plot_spearman(spearman_rows)
    plot_top_k_per_question(ranking_rows)
    plot_f1_minimal_comparison(min_rows, up3_rows)

    print("\nDone. All plots saved to:", PLOTS_DIR)
