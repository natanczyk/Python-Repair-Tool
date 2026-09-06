"""
Minimal set accuracy on Bench: LLM minimal_notests predictions vs FauxPy top-|GT|.

Direct parallel to table3_minimal_set_llm.py, but on the Bench dataset
(easy/medium/hard) using Data_Bench/question_<level>/ground_truth.jsonl.
Unlike Refactory, only the minimal_notests mode is used here (model sees
only the assignment description and code, no test I/O) since that is the
one mode all 8 models have complete Bench results for.

FauxPy has no minimal-set prediction mode, so its predicted set is the
top-k lines of its ranking, k = size of ground truth for that submission
-- identical treatment to table3_minimal_set_llm.py's Refactory baseline.

All predicted sets are compared to ground truth with set-based
Precision / Recall / F1.
"""

from __future__ import annotations

from common import (
    MODELS, MODEL_LABELS, OUT_TABLES,
    load_ground_truth, load_fauxpy_ranking, load_llm_minimal_notests,
    per_submission_scores, aggregate,
)

import pandas as pd


def build_table1(gt: dict) -> tuple[pd.DataFrame, dict[str, dict[str, tuple[float, float, float]]]]:
    rows = []
    per_model_scores: dict[str, dict[str, tuple[float, float, float]]] = {}

    fauxpy_scores = per_submission_scores(gt, load_fauxpy_ranking(), top_k_ranking=True)
    per_model_scores["fauxpy"] = fauxpy_scores
    rows.append({"Method": "FauxPy", **{k: v for k, v in aggregate(fauxpy_scores).items() if k != "n"}})

    for model in MODELS:
        scores = per_submission_scores(gt, load_llm_minimal_notests(model), top_k_ranking=False)
        per_model_scores[model] = scores
        rows.append({"Method": MODEL_LABELS[model], **{k: v for k, v in aggregate(scores).items() if k != "n"}})

    return pd.DataFrame(rows).set_index("Method"), per_model_scores


if __name__ == "__main__":
    gt = load_ground_truth()

    print(f"Minimal set accuracy on Bench: LLM minimal_notests predictions vs FauxPy top-|GT|")
    print(f"Ground truth: {len(gt)} Bench submissions (easy/medium/hard)\n")

    table1, per_model_scores = build_table1(gt)
    table1 = table1.round(3)
    print(table1.to_string())

    csv_path = OUT_TABLES / "table1_bench_minimal_set_llm.csv"
    table1.to_csv(csv_path)
    print(f"\n[saved] {csv_path}")