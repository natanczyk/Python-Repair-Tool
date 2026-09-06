"""
Shared constants and data loading for the Refactory repair-loop analysis.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT        = Path(__file__).parent.parent.parent
REPAIR_ROOT = ROOT / "results_v2" / "refactory_repair"
DATA_ROOT   = ROOT / "Data"
OUT_TABLES  = Path(__file__).parent / "tables"
OUT_FIGURES = Path(__file__).parent / "figures"
OUT_TABLES.mkdir(exist_ok=True)
OUT_FIGURES.mkdir(exist_ok=True)

QUESTIONS = [1, 2, 3, 4, 5]
TYPES = ["none", "fauxpy", "best_loc", "self_llm"]
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

TYPE_LABELS = {
    "none":     "None",
    "fauxpy":   "FauxPy",
    "best_loc": "Best-Loc (Gemma4)",
    "self_llm": "Self-LLM",
}

# Models whose standalone localization showed prompt-anchoring bias
# (predictions defaulting toward the ranking prompt's own worked example).
ANCHORING_MODELS = ["granite_code", "codegemma", "qwen"]

MAX_ATTEMPTS = 4

# Question 2 is incomplete or entirely absent for gemma4, granite4,
# granite_code, and codellama (granite_code/codellama skip it outright;
# gemma4/granite4 have partial best_loc and no self_llm at all). It's also
# the exercise later skipped deliberately for new runs because it was
# "almost always failing after 4 tries". Cross-model comparisons exclude it
# so every model is compared on the same 4-question, 1,348-submission basis;
# the per-question analysis (table6) uses only the 4 fully-complete models
# to characterize question 2 on its own terms.
COMPARABLE_QUESTIONS = [1, 3, 4, 5]
FULLY_COMPLETE_MODELS = ["qwen", "qwen3_27b", "qwen3_coder", "codegemma"]


def comparable(df: pd.DataFrame) -> pd.DataFrame:
    """Restrict to the 4-question basis every model has in common."""
    return df[df["question"].isin(COMPARABLE_QUESTIONS)].copy()


def load_records() -> pd.DataFrame:
    """One row per (question, repair_type, repair_model, submission)."""
    rows = []
    for q in QUESTIONS:
        for t in TYPES:
            for model in MODELS:
                p = REPAIR_ROOT / f"question_{q}" / f"repair_{t}_{model}_results.jsonl"
                if not p.exists():
                    continue
                for line in p.read_text(encoding="utf-8").splitlines():
                    if not line.strip():
                        continue
                    r = json.loads(line)
                    rows.append({
                        "question": q,
                        "repair_type": t,
                        "repair_model": model,
                        "submission": r["submission"],
                        "solved": bool(r["solved"]),
                        "iterations": int(r["iterations"]),
                    })
    df = pd.DataFrame(rows)
    df["model_label"] = df["repair_model"].map(MODEL_LABELS)
    df["type_label"] = df["repair_type"].map(TYPE_LABELS)
    return df


def load_ground_truth_sizes() -> dict[tuple[int, str], int]:
    """(question, submission) -> number of ground-truth buggy lines."""
    sizes: dict[tuple[int, str], int] = {}
    for q in QUESTIONS:
        p = DATA_ROOT / f"question_{q}" / "ground_truth.jsonl"
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            sizes[(q, r["program_name"])] = len(r["buggy_lines"])
    return sizes