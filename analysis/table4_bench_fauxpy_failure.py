"""
Table 4. FauxPy failure analysis on the Bench dataset

Data_Bench/question_<level>/metadata.jsonl tags every submission with an
injected-bug category (syntax error, logic error, reference error, multiple
error) and subtype. Cross-referencing that against FauxPy's output
(results_v2/Bench_loc/question_<level>/fauxpy_localization.jsonl) shows
*which kinds* of bugs FauxPy fails to localize (empty buggy_lines), not just
an aggregate failure rate.

FauxPy is spectrum-based (SBFL): it needs the test suite to actually execute
the program and record per-line coverage across passing/failing runs. A
program that cannot be parsed or imported produces no coverage trace at all,
so FauxPy has nothing to rank -- it returns an empty list. This predicts a
near-100% failure rate specifically on the "syntax error" category and (to
a lesser extent) "reference error" (undefined names -> crash on import/call),
while "logic error" (code runs, produces a wrong result) is exactly the
case SBFL was designed for.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT      = Path(__file__).parent.parent
DATA_BENCH = ROOT / "Data_Bench"
BENCH_LOC  = ROOT / "results_v2" / "Bench_loc"
OUT_DIR    = Path(__file__).parent / "tables"
OUT_DIR.mkdir(exist_ok=True)

LEVELS = ["easy", "medium", "hard"]


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def load_metadata(level: str) -> dict[str, dict]:
    rows = load_jsonl(DATA_BENCH / f"question_{level}" / "metadata.jsonl")
    return {r["program_name"]: r for r in rows}


def load_fauxpy(level: str) -> dict[str, list[int]]:
    rows = load_jsonl(BENCH_LOC / f"question_{level}" / "fauxpy_localization.jsonl")
    return {r["program_name"]: r["buggy_lines"] for r in rows}


def build_category_table() -> pd.DataFrame:
    counts: dict[str, dict[str, int]] = {}
    for level in LEVELS:
        meta = load_metadata(level)
        fx = load_fauxpy(level)
        for prog, m in meta.items():
            cat = m.get("category", "unknown")
            counts.setdefault(cat, {"total": 0, "empty": 0, "no_run": 0})
            if prog not in fx:
                counts[cat]["no_run"] += 1
                continue
            counts[cat]["total"] += 1
            if not fx[prog]:
                counts[cat]["empty"] += 1

    rows = []
    for cat, c in counts.items():
        total = c["total"]
        rows.append({
            "Category": cat,
            "N (has FauxPy output)": total,
            "N (FauxPy never ran / no record)": c["no_run"],
            "Empty predictions": c["empty"],
            "Empty rate": (c["empty"] / total) if total else float("nan"),
        })
    df = pd.DataFrame(rows).set_index("Category")
    return df.sort_values("Empty rate", ascending=False)


def build_level_table() -> pd.DataFrame:
    rows = []
    for level in LEVELS:
        meta = load_metadata(level)
        fx = load_fauxpy(level)
        total_meta = len(meta)
        total_fx = len(fx)
        empty = sum(1 for v in fx.values() if not v)
        no_run = total_meta - total_fx
        rows.append({
            "Level": level,
            "Total submissions": total_meta,
            "FauxPy has no record": no_run,
            "Empty predictions": empty,
            "Empty rate (of those run)": (empty / total_fx) if total_fx else float("nan"),
        })
    return pd.DataFrame(rows).set_index("Level")


if __name__ == "__main__":
    level_table = build_level_table()
    print("=== FauxPy outcome by difficulty level ===\n")
    print(level_table.round(3).to_string())

    cat_table = build_category_table()
    print("\n\n=== FauxPy outcome by injected-bug category (all levels combined) ===\n")
    print(cat_table.round(3).to_string())

    level_table.round(3).to_csv(OUT_DIR / "table4_bench_fauxpy_by_level.csv")
    cat_table.round(3).to_csv(OUT_DIR / "table4_bench_fauxpy_by_category.csv")
    print(f"\n[saved] {OUT_DIR / 'table4_bench_fauxpy_by_level.csv'}")
    print(f"[saved] {OUT_DIR / 'table4_bench_fauxpy_by_category.csv'}")
