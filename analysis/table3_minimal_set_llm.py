"""
Table 3. Minimal set accuracy (actual LLM minimal-set predictions)

Unlike Table 1 (which derives a "minimal set" for LLMs by slicing their
ranking to the top-|GT| lines), this table uses the LLMs' own minimal-set
predictions directly: llm_<model>_minimal_localization.jsonl (model given
failing test output and asked to name the exact set of buggy lines).

FauxPy has no minimal-set prediction mode, so its predicted set is the top-k
lines of its ranking, k = size of ground truth for that submission.

All predicted sets are compared to ground truth with set-based
Precision / Recall / F1. No ranking metrics (Top-k, MRR) are included.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT      = Path(__file__).parent.parent
REF_LOC   = ROOT / "results_v2" / "refactory_loc"
DATA      = ROOT / "Data"
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


def load_ground_truth() -> dict[str, list[int]]:
    gt = {}
    for q in QUESTIONS:
        gt.update(load_jsonl(DATA / f"question_{q}" / "ground_truth.jsonl"))
    return gt


def load_fauxpy_ranking() -> dict[str, list[int]]:
    preds = {}
    for q in QUESTIONS:
        preds.update(load_jsonl(REF_LOC / f"question_{q}" / "fauxpy_localization.jsonl"))
    return preds


def load_llm_minimal_set(model: str) -> dict[str, list[int]]:
    """LLM's own minimal-set prediction, with test feedback."""
    preds = {}
    for q in QUESTIONS:
        preds.update(load_jsonl(REF_LOC / f"question_{q}" / f"llm_{model}_minimal_localization.jsonl"))
    return preds


def prf(pred_set: set[int], gt_set: set[int]) -> tuple[float, float, float]:
    if not pred_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gt_set)
    p = tp / len(pred_set)
    r = tp / len(gt_set)
    f1 = (2 * p * r / (p + r)) if (p + r) > 0 else 0.0
    return p, r, f1


def compute_fauxpy_metrics(gt: dict) -> dict:
    ranking = load_fauxpy_ranking()
    common = [name for name in gt if name in ranking]
    precs, recs, f1s = [], [], []
    for name in common:
        gt_set = set(gt[name])
        if not gt_set:
            continue
        pred_set = set(ranking[name][:len(gt_set)])
        p, r, f1 = prf(pred_set, gt_set)
        precs.append(p)
        recs.append(r)
        f1s.append(f1)
    return {
        "n": len(precs),
        "Precision": np.mean(precs) if precs else 0.0,
        "Recall":    np.mean(recs) if recs else 0.0,
        "F1":        np.mean(f1s) if f1s else 0.0,
    }


def compute_llm_metrics(gt: dict, model: str) -> dict:
    preds = load_llm_minimal_set(model)
    common = [name for name in gt if name in preds]
    precs, recs, f1s = [], [], []
    for name in common:
        gt_set = set(gt[name])
        if not gt_set:
            continue
        pred_set = set(preds[name])
        p, r, f1 = prf(pred_set, gt_set)
        precs.append(p)
        recs.append(r)
        f1s.append(f1)
    return {
        "n": len(precs),
        "Precision": np.mean(precs) if precs else 0.0,
        "Recall":    np.mean(recs) if recs else 0.0,
        "F1":        np.mean(f1s) if f1s else 0.0,
    }


def build_table3() -> pd.DataFrame:
    gt = load_ground_truth()
    rows = []

    fauxpy_metrics = compute_fauxpy_metrics(gt)
    rows.append({"Method": "FauxPy", **{k: v for k, v in fauxpy_metrics.items() if k != "n"}})

    for model in MODELS:
        metrics = compute_llm_metrics(gt, model)
        rows.append({"Method": MODEL_LABELS[model], **{k: v for k, v in metrics.items() if k != "n"}})

    return pd.DataFrame(rows).set_index("Method")


if __name__ == "__main__":
    gt = load_ground_truth()
    table3 = build_table3().round(3)

    print(f"Minimal set accuracy: LLM minimal-set predictions (with tests) vs FauxPy top-|GT|")
    print(f"Ground truth: {len(gt)} Refactory submissions (questions 1-5)\n")
    print(table3.to_string())

    csv_path = OUT_DIR / "table3_minimal_set_llm.csv"
    table3.to_csv(csv_path)
    print(f"\n[saved] {csv_path}")
