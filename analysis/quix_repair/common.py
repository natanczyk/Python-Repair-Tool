"""
Shared constants and data loading for the QuixBugs repair-loop analysis.
Mirrors analysis/refactory_repair/common.py's logic, adapted for two
structural differences from Refactory:

  1. QuixBugs results were downloaded already merged into flat files
     (results_v2/quixbugs_repair/repair_<type>_<model>_results.jsonl)
     rather than per-question folders, so there is no per-question loop
     when reading them.
  2. Each result record has no "question" field of its own (same as
     Refactory) -- but unlike Refactory, there's no separate per-question
     source directory to infer it from either, since the files are already
     merged. Question number is instead recovered by matching the
     submission's program name (wrong_<name>.py) against
     Data_QuixBugs/manifest.json's question_N -> name mapping.

There is no Refactory-style COMPARABLE_QUESTIONS / FULLY_COMPLETE_MODELS
restriction here: all 40 questions and all 8 models are used directly,
since (unlike Refactory's question 2) QuixBugs has no known-bad question
requiring exclusion. If a model's data is still incomplete for some
combination, the per-table dropna/filtering already handles it gracefully.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT        = Path(__file__).parent.parent.parent
REPAIR_ROOT = ROOT / "results_v2" / "quixbugs_repair"
DATA_ROOT   = ROOT / "Data_QuixBugs"
OUT_TABLES  = Path(__file__).parent / "tables"
OUT_FIGURES = Path(__file__).parent / "figures"
OUT_TABLES.mkdir(exist_ok=True)
OUT_FIGURES.mkdir(exist_ok=True)

QUESTIONS = list(range(1, 41))
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

# Carried over from the Refactory localization chapter's finding (same
# models, same classification) -- not independently re-derived for
# QuixBugs, but kept for a direct visual comparison between the two.
ANCHORING_MODELS = ["granite_code", "codegemma", "qwen"]

MAX_ATTEMPTS = 4


def _question_lookup() -> dict[str, int]:
    """{'wrong_<name>.py': question_N} from manifest.json."""
    manifest = json.loads((DATA_ROOT / "manifest.json").read_text(encoding="utf-8"))
    lookup = {}
    for key, info in manifest.items():
        q = int(key.removeprefix("question_"))
        lookup[f"wrong_{info['name']}.py"] = q
    return lookup


def comparable(df: pd.DataFrame) -> pd.DataFrame:
    """No-op here (kept only so ported table scripts can call it uniformly
    with the Refactory versions) -- QuixBugs has no excluded question."""
    return df


def load_records() -> pd.DataFrame:
    """One row per (question, repair_type, repair_model, submission)."""
    q_lookup = _question_lookup()
    rows = []
    for t in TYPES:
        for model in MODELS:
            p = REPAIR_ROOT / f"repair_{t}_{model}_results.jsonl"
            if not p.exists():
                continue
            for line in p.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                r = json.loads(line)
                rows.append({
                    "question": q_lookup.get(r["submission"]),
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