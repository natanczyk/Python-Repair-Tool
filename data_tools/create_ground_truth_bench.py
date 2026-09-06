"""
Creates ground_truth.jsonl for Data_Bench, one per difficulty level, using the
same diff algorithm as create_ground_truth.py (Refactory) and
prepare_quixbugs_data.py (QuixBugs) for methodological consistency across all
three datasets.

Unlike Refactory, Data_Bench has a direct 1:1 wrong <-> reference mapping per
submission (from metadata.jsonl's "reference_name" field) -- no CSV, no
multi-candidate correct-file matching needed.

Usage:
  python create_ground_truth_bench.py
  python create_ground_truth_bench.py --levels easy medium
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
BENCH_ROOT = ROOT / "Data_Bench"
LEVELS = ("easy", "medium", "hard")


# ---------------------------------------------------------------------------
# Line helpers (identical to create_ground_truth.py / prepare_quixbugs_data.py)
# ---------------------------------------------------------------------------

def normalize(line: str) -> str:
    rstripped = line.rstrip()
    indent = len(rstripped) - len(rstripped.lstrip())
    content = re.sub(r" {2,}", " ", rstripped.strip())
    return " " * indent + content


def is_semantic(line: str, in_diff: bool = False) -> bool:
    s = line.strip()
    if not s or s.startswith("#"):
        return False
    if s == "pass" and not in_diff:
        return False
    if s in {"try:", "finally:"}:
        return False
    return True


def last_semantic_line(lines: list[str]) -> int | None:
    for i in range(len(lines) - 1, -1, -1):
        if is_semantic(lines[i], in_diff=False):
            return i + 1
    return None


def find_buggy_lines(wrong_lines: list[str], correct_lines: list[str]) -> list[int]:
    norm_wrong = [normalize(l) for l in wrong_lines]
    norm_correct = [normalize(l) for l in correct_lines]

    matcher = difflib.SequenceMatcher(None, norm_wrong, norm_correct, autojunk=False)
    total_wrong = sum(1 for l in wrong_lines if l.strip())

    candidates: list[int] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        if tag in ("replace", "delete"):
            block_size = i2 - i1
            if total_wrong > 0 and block_size / total_wrong > 0.5:
                continue
            for i in range(i1, i2):
                if is_semantic(wrong_lines[i], in_diff=True):
                    candidates.append(i + 1)
        elif tag == "insert":
            nearest = i1
            if nearest > 0 and is_semantic(wrong_lines[nearest - 1], in_diff=False):
                if nearest not in candidates:
                    candidates.append(nearest)

    if candidates:
        return candidates

    wrong_nonempty = sum(1 for l in wrong_lines if l.strip())
    correct_nonempty = sum(1 for l in correct_lines if l.strip())
    if wrong_nonempty < correct_nonempty:
        last = last_semantic_line(wrong_lines)
        if last:
            return [last]

    return []


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_level(level: str) -> dict:
    q_dir = BENCH_ROOT / f"question_{level}"
    wrong_dir = q_dir / "code" / "wrong"
    ref_dir = q_dir / "code" / "reference"
    metadata_file = q_dir / "metadata.jsonl"
    output_file = q_dir / "ground_truth.jsonl"

    rows = [json.loads(l) for l in metadata_file.read_text(encoding="utf-8").splitlines() if l.strip()]

    results: list[dict] = []
    empty = 0
    missing_files = 0
    by_category_empty: dict[str, int] = {}
    by_category_total: dict[str, int] = {}

    for row in rows:
        wrong_name = row["program_name"]
        ref_name = row["reference_name"]
        category = row.get("category", "unknown")

        wrong_path = wrong_dir / wrong_name
        ref_path = ref_dir / ref_name

        if not wrong_path.exists() or not ref_path.exists():
            missing_files += 1
            continue

        wrong_lines = wrong_path.read_text(encoding="utf-8").splitlines()
        correct_lines = ref_path.read_text(encoding="utf-8").splitlines()

        buggy = find_buggy_lines(wrong_lines, correct_lines)

        by_category_total[category] = by_category_total.get(category, 0) + 1
        if not buggy:
            empty += 1
            by_category_empty[category] = by_category_empty.get(category, 0) + 1

        results.append({"program_name": wrong_name, "buggy_lines": buggy})

    output_file.write_text(
        "\n".join(json.dumps(r) for r in results) + "\n",
        encoding="utf-8",
    )

    return {
        "level": level,
        "total": len(results),
        "empty": empty,
        "missing_files": missing_files,
        "by_category_total": by_category_total,
        "by_category_empty": by_category_empty,
        "output_file": output_file,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--levels", nargs="+", default=list(LEVELS), choices=list(LEVELS))
    args = parser.parse_args()

    all_stats = []
    for level in args.levels:
        stats = process_level(level)
        all_stats.append(stats)
        print(f"\n=== {level} ===")
        print(f"  Wrote {stats['total']} entries to {stats['output_file']}")
        print(f"  Empty buggy_lines: {stats['empty']} ({stats['empty']/stats['total']:.1%})" if stats['total'] else "  Empty buggy_lines: 0")
        if stats["missing_files"]:
            print(f"  [warn] Missing wrong/reference file pairs skipped: {stats['missing_files']}")
        print("  Empty rate by category:")
        for cat, total in sorted(stats["by_category_total"].items(), key=lambda x: -x[1]):
            emp = stats["by_category_empty"].get(cat, 0)
            print(f"    {cat:20s} {emp:4d}/{total:4d}  ({emp/total:.1%})")

    print("\n=== Overall ===")
    total_all = sum(s["total"] for s in all_stats)
    empty_all = sum(s["empty"] for s in all_stats)
    print(f"  {empty_all}/{total_all} empty ({empty_all/total_all:.1%})" if total_all else "  0 entries")


if __name__ == "__main__":
    main()