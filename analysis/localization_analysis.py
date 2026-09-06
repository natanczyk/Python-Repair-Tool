"""
Localization analysis script.
# -*- coding: utf-8 -*-


Produces:
  - Refactory: Top-k, MFR, Precision/Recall/F1 tables + bar charts
  - Bench: FauxPy empty rate, prediction coverage, set-size distribution
"""

from __future__ import annotations

import json
from pathlib import Path
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ── paths ─────────────────────────────────────────────────────────────────────

ROOT        = Path(__file__).parent.parent
RESULTS     = ROOT / "results_v2"
REF_LOC     = RESULTS / "refactory_loc"
BENCH_LOC   = RESULTS / "Bench_loc"
DATA        = ROOT / "Data"
OUT         = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

QUESTIONS   = [1, 2, 3, 4, 5]
BENCH_LEVELS = ["easy", "medium", "hard"]

MODELS = [
    "qwen", "qwen3_27b", "qwen3_coder",
    "gemma4", "granite4",
    "codegemma", "granite_code", "codellama",
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

MODES = ["fauxpy", "ranking", "minimal_tests", "minimal_notests"]
MODE_LABELS = {
    "fauxpy":           "FauxPy (SBFL)",
    "ranking":          "LLM Ranking",
    "minimal_tests":    "LLM Minimal + Tests",
    "minimal_notests":  "LLM Minimal (no tests)",
}

MODE_FILE_SUFFIX = {
    "fauxpy":          "fauxpy_localization",
    "ranking":         "localization",
    "minimal_tests":   "minimal_localization",
    "minimal_notests": "minimal_notests_localization",
}

COLORS = {
    "fauxpy":          "#E07B39",
    "ranking":         "#4878CF",
    "minimal_tests":   "#6ACC65",
    "minimal_notests": "#D65F5F",
}

# ── data loading ──────────────────────────────────────────────────────────────

def load_jsonl(path: Path) -> dict[str, list[int]]:
    """Returns {program_name: buggy_lines}."""
    data = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            data[r["program_name"]] = r["buggy_lines"]
    return data


def load_ground_truth() -> dict[str, list[int]]:
    """Merge ground truth across all 5 questions."""
    gt = {}
    for q in QUESTIONS:
        path = DATA / f"question_{q}" / "ground_truth.jsonl"
        gt.update(load_jsonl(path))
    return gt


def load_predictions(model: str, mode: str) -> dict[str, list[int]]:
    """Merge predictions for one model/mode across all 5 questions.
    For fauxpy mode, model is ignored and the shared fauxpy file is used."""
    preds = {}
    for q in QUESTIONS:
        if mode == "fauxpy":
            path = REF_LOC / f"question_{q}" / "fauxpy_localization.jsonl"
        else:
            suffix = MODE_FILE_SUFFIX[mode]
            path = REF_LOC / f"question_{q}" / f"llm_{model}_{suffix}.jsonl"
        if path.exists():
            preds.update(load_jsonl(path))
    return preds


def load_bench_predictions(model: str, mode: str) -> dict[str, list[int]]:
    suffix = MODE_FILE_SUFFIX[mode]
    preds = {}
    for level in BENCH_LEVELS:
        path = BENCH_LOC / f"question_{level}" / f"llm_{model}_{suffix}.jsonl"
        if path.exists():
            preds.update(load_jsonl(path))
    return preds


def load_bench_fauxpy() -> dict[str, list[int]]:
    preds = {}
    for level in BENCH_LEVELS:
        path = BENCH_LOC / f"question_{level}" / "fauxpy_localization.jsonl"
        if path.exists():
            preds.update(load_jsonl(path))
    return preds

# ── metric functions ──────────────────────────────────────────────────────────

def acc_at_k(pred: list[int], gt_set: set[int], k: int) -> int:
    return int(bool(set(pred[:k]) & gt_set))


def first_rank(pred: list[int], gt_set: set[int]) -> int | None:
    for i, line in enumerate(pred, 1):
        if line in gt_set:
            return i
    return None


def prf(pred_set: set[int], gt_set: set[int]) -> tuple[float, float, float]:
    if not pred_set and not gt_set:
        return 1.0, 1.0, 1.0
    if not pred_set or not gt_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gt_set)
    p  = tp / len(pred_set)
    r  = tp / len(gt_set)
    f1 = (2 * p * r / (p + r)) if (p + r) > 0 else 0.0
    return p, r, f1


def compute_refactory_metrics(gt: dict, model: str, mode: str) -> dict:
    preds = load_predictions(model, mode)
    common = [k for k in gt if k in preds]

    accs   = {1: [], 3: [], 5: []}
    mfrs   = []
    precs, recs, f1s = [], [], []

    for name in common:
        pred   = preds[name]
        gt_set = set(gt[name])
        if not gt_set:
            continue

        for k in [1, 3, 5]:
            accs[k].append(acc_at_k(pred, gt_set, k))

        if mode in ("ranking", "fauxpy"):
            fr = first_rank(pred, gt_set)
            if fr is not None:
                mfrs.append(fr)
            else:
                mfrs.append(len(pred) + 1)

            # For P/R/F1 on ranking/fauxpy: take top-|GT| lines
            pred_set = set(pred[:len(gt_set)])
        else:
            pred_set = set(pred)

        p, r, f1 = prf(pred_set, gt_set)
        precs.append(p)
        recs.append(r)
        f1s.append(f1)

    n = len(common)
    return {
        "n":         n,
        "acc@1":     np.mean(accs[1])  if accs[1]  else 0,
        "acc@3":     np.mean(accs[3])  if accs[3]  else 0,
        "acc@5":     np.mean(accs[5])  if accs[5]  else 0,
        "mfr":       np.mean(mfrs)     if mfrs     else None,
        "precision": np.mean(precs)    if precs    else 0,
        "recall":    np.mean(recs)     if recs     else 0,
        "f1":        np.mean(f1s)      if f1s      else 0,
    }

# ── printing helpers ──────────────────────────────────────────────────────────

def print_table(title: str, headers: list[str], rows: list[list]) -> None:
    col_w = [max(len(str(h)), max(len(str(r[i])) for r in rows))
             for i, h in enumerate(headers)]
    sep = "+" + "+".join("-" * (w + 2) for w in col_w) + "+"
    fmt = "|" + "|".join(f" {{:<{w}}} " for w in col_w) + "|"
    print(f"\n{'='*len(sep)}")
    print(title.center(len(sep)))
    print('='*len(sep))
    print(sep)
    print(fmt.format(*headers))
    print(sep)
    for row in rows:
        print(fmt.format(*[str(v) for v in row]))
    print(sep)

# ── REFACTORY ANALYSIS ────────────────────────────────────────────────────────

def run_refactory_analysis():
    print("\n" + "="*70)
    print("  REFACTORY LOCALIZATION ANALYSIS")
    print("="*70)

    gt = load_ground_truth()
    total = len(gt)
    print(f"  Total submissions: {total} (across questions 1–5)")

    # FauxPy is model-independent — compute once
    fauxpy_metrics = compute_refactory_metrics(gt, model="", mode="fauxpy")

    # LLM results: model × mode (only LLM modes)
    LLM_MODES = ["ranking", "minimal_tests", "minimal_notests"]
    results: dict[tuple, dict] = {}
    for model in MODELS:
        for mode in LLM_MODES:
            results[(model, mode)] = compute_refactory_metrics(gt, model, mode)

    # ── Top-k hit rate ───────────────────────────────────────────────────────
    headers = ["Model", "Mode", "Top-1", "Top-3", "Top-5"]
    rows = []
    # FauxPy row first
    rows.append([
        "FauxPy (SBFL)", "—",
        f"{fauxpy_metrics['acc@1']:.3f}",
        f"{fauxpy_metrics['acc@3']:.3f}",
        f"{fauxpy_metrics['acc@5']:.3f}",
    ])
    for model in MODELS:
        for mode in LLM_MODES:
            m = results[(model, mode)]
            rows.append([
                MODEL_LABELS[model], MODE_LABELS[mode],
                f"{m['acc@1']:.3f}", f"{m['acc@3']:.3f}", f"{m['acc@5']:.3f}",
            ])
    print_table("Top-k hit rate (proportion of submissions with ≥1 correct line in top k)", headers, rows)

    # ── Mean First Rank (ranking methods) ───────────────────────────────────
    headers = ["Model", "Mode", "MFR (↓ better)"]
    rows = []
    rows.append(["FauxPy (SBFL)", "—",
                 f"{fauxpy_metrics['mfr']:.2f}" if fauxpy_metrics["mfr"] else "N/A"])
    for model in MODELS:
        m = results[(model, "ranking")]
        rows.append([MODEL_LABELS[model], "LLM Ranking",
                     f"{m['mfr']:.2f}" if m["mfr"] else "N/A"])
    print_table("Mean First Rank (ranking methods, lower is better)", headers, rows)

    # ── Top-1 grouped bar chart ──────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 5))
    x     = np.arange(len(MODELS))
    width = 0.22
    for i, mode in enumerate(LLM_MODES):
        vals = [results[(m, mode)]["acc@1"] for m in MODELS]
        ax.bar(x + i * width, vals, width, label=MODE_LABELS[mode],
               color=COLORS[mode], alpha=0.88)
    # FauxPy as horizontal reference line
    ax.axhline(fauxpy_metrics["acc@1"], color=COLORS["fauxpy"],
               linestyle="--", linewidth=1.8, label=f"FauxPy (SBFL) = {fauxpy_metrics['acc@1']:.3f}")
    ax.set_xticks(x + width)
    ax.set_xticklabels([MODEL_LABELS[m] for m in MODELS], rotation=25, ha="right", fontsize=9)
    ax.set_ylabel("Top-1")
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_title("Top-1 by Model and Localization Mode (Refactory)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "fig1_acc1_refactory.png", dpi=150)
    plt.close()
    print(f"\n  [saved] fig1_acc1_refactory.png")

    # ── Top-1/3/5 per LLM mode subplot ───────────────────────────────────────
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    for ax, mode in zip(axes, LLM_MODES):
        vals1 = [results[(m, mode)]["acc@1"] for m in MODELS]
        vals3 = [results[(m, mode)]["acc@3"] for m in MODELS]
        vals5 = [results[(m, mode)]["acc@5"] for m in MODELS]
        x = np.arange(len(MODELS))
        w = 0.25
        ax.bar(x - w, vals1, w, label="Top-1", color="#4878CF", alpha=0.88)
        ax.bar(x,     vals3, w, label="Top-3", color="#6ACC65", alpha=0.88)
        ax.bar(x + w, vals5, w, label="Top-5", color="#D65F5F", alpha=0.88)
        # FauxPy reference lines
        ax.axhline(fauxpy_metrics["acc@1"], color="#E07B39", linestyle=":", linewidth=1.4, label="FauxPy Top-1")
        ax.axhline(fauxpy_metrics["acc@3"], color="#E07B39", linestyle="--", linewidth=1.4, label="FauxPy Top-3")
        ax.axhline(fauxpy_metrics["acc@5"], color="#E07B39", linestyle="-", linewidth=1.4, label="FauxPy Top-5")
        ax.set_title(MODE_LABELS[mode], fontsize=10)
        ax.set_xticks(x)
        ax.set_xticklabels([MODEL_LABELS[m] for m in MODELS], rotation=30, ha="right", fontsize=8)
        ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
        ax.set_ylim(0, 1.05)
        ax.grid(axis="y", alpha=0.3)
        if ax == axes[0]:
            ax.set_ylabel("Accuracy")
        ax.legend(fontsize=7)
    fig.suptitle("Top-k by Mode with FauxPy Reference (Refactory)", fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT / "fig2_accK_refactory.png", dpi=150)
    plt.close()
    print(f"  [saved] fig2_accK_refactory.png")

    # ── F1 grouped bar chart ─────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 5))
    x     = np.arange(len(MODELS))
    width = 0.22
    for i, mode in enumerate(LLM_MODES):
        vals = [results[(m, mode)]["f1"] for m in MODELS]
        ax.bar(x + i * width, vals, width, label=MODE_LABELS[mode],
               color=COLORS[mode], alpha=0.88)
    ax.axhline(fauxpy_metrics["f1"], color=COLORS["fauxpy"],
               linestyle="--", linewidth=1.8, label=f"FauxPy (SBFL) = {fauxpy_metrics['f1']:.3f}")
    ax.set_xticks(x + width)
    ax.set_xticklabels([MODEL_LABELS[m] for m in MODELS], rotation=25, ha="right", fontsize=9)
    ax.set_ylabel("F1 Score")
    ax.set_ylim(0, 1.0)
    ax.set_title("F1 Score by Model and Localization Mode (Refactory)")
    ax.legend(fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "fig3_f1_refactory.png", dpi=150)
    plt.close()
    print(f"  [saved] fig3_f1_refactory.png")

    # ── Mean First Rank — FauxPy + all models (ranking mode) ─────────────────
    fig, ax = plt.subplots(figsize=(10, 4))
    mfr_models  = [MODEL_LABELS[m] for m in MODELS]
    mfr_vals    = [results[(m, "ranking")]["mfr"] or 0 for m in MODELS]
    bar_colors  = ["#4878CF"] * len(MODELS)
    # prepend FauxPy
    all_labels  = ["FauxPy\n(SBFL)"] + mfr_models
    all_vals    = [fauxpy_metrics["mfr"] or 0] + mfr_vals
    all_colors  = [COLORS["fauxpy"]] + bar_colors
    bars = ax.bar(all_labels, all_vals, color=all_colors, alpha=0.88)
    for bar, v in zip(bars, all_vals):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                f"{v:.2f}", ha="center", va="bottom", fontsize=8)
    ax.set_ylabel("Mean First Rank (lower = better)")
    ax.set_title("Mean First Rank: FauxPy vs LLM Ranking (Refactory)")
    ax.set_xticklabels(all_labels, rotation=25, ha="right", fontsize=9)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "fig4_mfr_refactory.png", dpi=150)
    plt.close()
    print(f"  [saved] fig4_mfr_refactory.png")

    # ── Precision / Recall / F1 grouped bar charts ───────────────────────────
    # All methods evaluated as set comparison:
    #   FauxPy & LLM Ranking: top-|GT| lines vs GT
    #   LLM Minimal methods:  full predicted set vs GT
    SET_MODES = ["ranking", "minimal_tests", "minimal_notests"]
    SET_MODE_COLORS = {
        "ranking":         "#4878CF",
        "minimal_tests":   "#6ACC65",
        "minimal_notests": "#D65F5F",
    }

    for metric, metric_label in [
        ("precision", "Precision"),
        ("recall",    "Recall"),
        ("f1",        "F1-Score"),
    ]:
        fig, ax = plt.subplots(figsize=(14, 5))
        x     = np.arange(len(MODELS))
        width = 0.20
        for i, mode in enumerate(SET_MODES):
            vals = [results[(m, mode)][metric] for m in MODELS]
            bars = ax.bar(x + i * width, vals, width,
                          label=MODE_LABELS[mode],
                          color=SET_MODE_COLORS[mode], alpha=0.88)
        # FauxPy as horizontal reference line
        fval = fauxpy_metrics[metric]
        ax.axhline(fval, color=COLORS["fauxpy"], linestyle="--", linewidth=2.0,
                   label=f"FauxPy top-|GT| = {fval:.3f}")
        ax.set_xticks(x + width)
        ax.set_xticklabels([MODEL_LABELS[m] for m in MODELS], rotation=25, ha="right", fontsize=9)
        ax.set_ylabel(metric_label)
        ax.set_ylim(0, 1.0)
        ax.set_title(f"{metric_label}: Set-Based Comparison vs Ground Truth (Refactory)")
        ax.legend(fontsize=9)
        ax.grid(axis="y", alpha=0.3)
        plt.tight_layout()
        fname = f"fig5_{metric}_refactory.png"
        plt.savefig(OUT / fname, dpi=150)
        plt.close()
        print(f"  [saved] {fname}")

    # ── Full P/R/F1 set-based comparison ─────────────────────────────────────
    headers = ["Model", "Mode", "Precision", "Recall", "F1"]
    rows = []
    rows.append([
        "FauxPy (SBFL)", "top-|GT| lines",
        f"{fauxpy_metrics['precision']:.3f}",
        f"{fauxpy_metrics['recall']:.3f}",
        f"{fauxpy_metrics['f1']:.3f}",
    ])
    for model in MODELS:
        first = True
        for mode in SET_MODES:
            m = results[(model, mode)]
            mode_label = MODE_LABELS[mode] if mode != "ranking" else "LLM Ranking (top-|GT|)"
            rows.append([
                MODEL_LABELS[model] if first else "",
                mode_label,
                f"{m['precision']:.3f}", f"{m['recall']:.3f}", f"{m['f1']:.3f}",
            ])
            first = False
    print_table(
        "Set-Based P/R/F1: FauxPy top-|GT| vs LLM Methods (Refactory)",
        headers, rows
    )


# ── BENCH ANALYSIS ────────────────────────────────────────────────────────────

BENCH_MODELS = ["qwen", "qwen3_27b", "qwen3_coder", "codegemma", "codellama"]

def run_bench_analysis():
    print("\n" + "="*70)
    print("  BENCH LOCALIZATION ANALYSIS")
    print("="*70)

    # ── Analysis 1: FauxPy empty rate by difficulty level ───────────────────
    print("\n  Analysis 1: FauxPy empty rate by difficulty level")
    fauxpy_all = {}
    for level in BENCH_LEVELS:
        path = BENCH_LOC / f"question_{level}" / "fauxpy_localization.jsonl"
        if path.exists():
            fauxpy_all[level] = load_jsonl(path)

    empty_rates = {}
    headers = ["Level", "Total", "Empty ([])", "Empty Rate"]
    rows = []
    for level in BENCH_LEVELS:
        data  = fauxpy_all.get(level, {})
        total = len(data)
        empty = sum(1 for v in data.values() if not v)
        rate  = empty / total if total else 0
        empty_rates[level] = rate
        rows.append([level.capitalize(), total, empty, f"{rate:.1%}"])
    print_table("FauxPy Empty Predictions on Bench Dataset", headers, rows)

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar([l.capitalize() for l in BENCH_LEVELS],
                  [empty_rates[l] for l in BENCH_LEVELS],
                  color=["#6ACC65", "#4878CF", "#D65F5F"], alpha=0.88)
    for bar, level in zip(bars, BENCH_LEVELS):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.01,
                f"{empty_rates[level]:.1%}", ha="center", va="bottom", fontsize=10)
    ax.set_ylabel("Proportion of Submissions with Empty Prediction")
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_title("FauxPy Empty Rate by Difficulty (Bench)")
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "fig6_fauxpy_empty_bench.png", dpi=150)
    plt.close()
    print(f"  [saved] fig6_fauxpy_empty_bench.png")

    # ── Analysis 2: Prediction coverage (non-empty %) by model and mode ─────
    print("\n  Analysis 2: Prediction coverage by model and mode")
    BENCH_LLM_MODES = ["ranking", "minimal_tests", "minimal_notests"]
    coverage: dict[tuple, float] = {}
    headers = ["Model", "Mode", "Total", "Non-empty", "Coverage"]
    rows = []
    for model in BENCH_MODELS:
        for mode in BENCH_LLM_MODES:
            preds = load_bench_predictions(model, mode)
            total = len(preds)
            nonempty = sum(1 for v in preds.values() if v)
            cov = nonempty / total if total else 0
            coverage[(model, mode)] = cov
            rows.append([MODEL_LABELS[model], MODE_LABELS[mode], total, nonempty, f"{cov:.1%}"])
    print_table("Prediction Coverage (non-empty) on Bench Dataset", headers, rows)

    fig, ax = plt.subplots(figsize=(13, 5))
    x     = np.arange(len(BENCH_MODELS))
    width = 0.25
    for i, mode in enumerate(BENCH_LLM_MODES):
        vals = [coverage[(m, mode)] for m in BENCH_MODELS]
        ax.bar(x + i * width, vals, width, label=MODE_LABELS[mode],
               color=COLORS[mode], alpha=0.88)
    ax.set_xticks(x + width)
    ax.set_xticklabels([MODEL_LABELS[m] for m in BENCH_MODELS], rotation=20, ha="right", fontsize=9)
    ax.set_ylabel("Coverage (proportion non-empty)")
    ax.set_ylim(0, 1.05)
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    ax.set_title("Prediction Coverage by Model and Mode (Bench)")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "fig7_coverage_bench.png", dpi=150)
    plt.close()
    print(f"  [saved] fig7_coverage_bench.png")

    # ── Analysis 3: Predicted set size distribution ──────────────────────────
    print("\n  Analysis 3: Predicted set size distribution")

    # collect size distributions for each mode (aggregated across all bench models)
    size_by_mode: dict[str, list[int]] = defaultdict(list)
    for model in BENCH_MODELS:
        for mode in BENCH_LLM_MODES:
            preds = load_bench_predictions(model, mode)
            for v in preds.values():
                size_by_mode[mode].append(len(v))

    # also fauxpy
    fauxpy_sizes = [len(v) for data in fauxpy_all.values() for v in data.values()]

    headers = ["Source", "Mean size", "Median", "% empty", "% size 1", "% size 2-5", "% size >5"]
    rows = []
    for mode in BENCH_LLM_MODES:
        sizes = size_by_mode[mode]
        n = len(sizes)
        if n == 0:
            continue
        rows.append([
            MODE_LABELS[mode],
            f"{np.mean(sizes):.2f}",
            f"{np.median(sizes):.1f}",
            f"{100*sum(s==0 for s in sizes)/n:.1f}%",
            f"{100*sum(s==1 for s in sizes)/n:.1f}%",
            f"{100*sum(2<=s<=5 for s in sizes)/n:.1f}%",
            f"{100*sum(s>5 for s in sizes)/n:.1f}%",
        ])
    if fauxpy_sizes:
        n = len(fauxpy_sizes)
        rows.append([
            "FauxPy (SBFL)",
            f"{np.mean(fauxpy_sizes):.2f}",
            f"{np.median(fauxpy_sizes):.1f}",
            f"{100*sum(s==0 for s in fauxpy_sizes)/n:.1f}%",
            f"{100*sum(s==1 for s in fauxpy_sizes)/n:.1f}%",
            f"{100*sum(2<=s<=5 for s in fauxpy_sizes)/n:.1f}%",
            f"{100*sum(s>5 for s in fauxpy_sizes)/n:.1f}%",
        ])
    print_table("Predicted Set Size Distribution (Bench)", headers, rows)

    fig, axes = plt.subplots(1, 4, figsize=(16, 4), sharey=False)
    plot_items = [(MODE_LABELS[m], size_by_mode[m], COLORS[m]) for m in BENCH_LLM_MODES]
    if fauxpy_sizes:
        plot_items.append(("FauxPy", fauxpy_sizes, "#888888"))

    for ax, (label, sizes, color) in zip(axes, plot_items):
        bins = [0, 1, 2, 3, 4, 5, 6, 10, 20, max(sizes) + 1] if sizes else [0, 1]
        counts, edges = np.histogram(sizes, bins=bins)
        pcts = counts / len(sizes) * 100
        labels_x = [f"{int(edges[i])}" if edges[i+1]-edges[i]==1
                    else f"{int(edges[i])}–{int(edges[i+1])-1}"
                    for i in range(len(counts))]
        ax.bar(range(len(pcts)), pcts, color=color, alpha=0.85)
        ax.set_xticks(range(len(pcts)))
        ax.set_xticklabels(labels_x, rotation=45, ha="right", fontsize=7)
        ax.set_title(label, fontsize=9)
        ax.set_ylabel("% of predictions")
        ax.grid(axis="y", alpha=0.3)

    fig.suptitle("Predicted Set Size Distribution (Bench)", fontsize=11)
    plt.tight_layout()
    plt.savefig(OUT / "fig8_setsize_bench.png", dpi=150)
    plt.close()
    print(f"  [saved] fig8_setsize_bench.png")


# ── entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_refactory_analysis()
    run_bench_analysis()
    print(f"\n  All figures saved to: {OUT}\n")
