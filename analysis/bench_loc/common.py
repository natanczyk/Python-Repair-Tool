"""
Shared constants and data loading for the Bench localization analysis.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT       = Path(__file__).parent.parent.parent
BENCH_LOC  = ROOT / "results_v2" / "Bench_loc"
DATA_BENCH = ROOT / "Data_Bench"
OUT_TABLES  = Path(__file__).parent / "tables"
OUT_FIGURES = Path(__file__).parent / "figures"
OUT_TABLES.mkdir(exist_ok=True)
OUT_FIGURES.mkdir(exist_ok=True)

LEVELS = ["easy", "medium", "hard"]

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
    for lvl in LEVELS:
        gt.update(load_jsonl(DATA_BENCH / f"question_{lvl}" / "ground_truth.jsonl"))
    return gt


def load_metadata() -> dict[str, str]:
    """Returns {program_name: category}."""
    meta = {}
    for lvl in LEVELS:
        path = DATA_BENCH / f"question_{lvl}" / "metadata.jsonl"
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                meta[r["program_name"]] = r.get("category", "unknown")
    return meta


def load_fauxpy_ranking() -> dict[str, list[int]]:
    preds = {}
    for lvl in LEVELS:
        preds.update(load_jsonl(BENCH_LOC / f"question_{lvl}" / "fauxpy_localization.jsonl"))
    return preds


def load_llm_minimal_notests(model: str) -> dict[str, list[int]]:
    preds = {}
    for lvl in LEVELS:
        preds.update(load_jsonl(BENCH_LOC / f"question_{lvl}" / f"llm_{model}_minimal_notests_localization.jsonl"))
    return preds


def prf(pred_set: set[int], gt_set: set[int]) -> tuple[float, float, float]:
    if not pred_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gt_set)
    p = tp / len(pred_set)
    r = tp / len(gt_set)
    f1 = (2 * p * r / (p + r)) if (p + r) > 0 else 0.0
    return p, r, f1


def per_submission_scores(gt: dict, preds: dict, top_k_ranking: bool) -> dict[str, tuple[float, float, float]]:
    """Returns {program_name: (p, r, f1)}. If top_k_ranking, the predicted
    set is the top-|GT| lines of the ranking (FauxPy); otherwise the full
    predicted set is used as-is (LLM minimal-set predictions)."""
    scores = {}
    for name in gt:
        if name not in preds:
            continue
        gt_set = set(gt[name])
        if not gt_set:
            continue
        pred = preds[name]
        pred_set = set(pred[:len(gt_set)]) if top_k_ranking else set(pred)
        scores[name] = prf(pred_set, gt_set)
    return scores


def aggregate(scores: dict[str, tuple[float, float, float]]) -> dict:
    if not scores:
        return {"n": 0, "Precision": 0.0, "Recall": 0.0, "F1": 0.0}
    precs = [v[0] for v in scores.values()]
    recs  = [v[1] for v in scores.values()]
    f1s   = [v[2] for v in scores.values()]
    return {
        "n": len(scores),
        "Precision": float(np.mean(precs)),
        "Recall":    float(np.mean(recs)),
        "F1":        float(np.mean(f1s)),
    }