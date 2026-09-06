"""
Creates a ground-truth fault localization JSONL dataset.

Strategy (applied in order):
  1. Try Refactored Correct Code from the CSV (de-tokenized via ast.unparse).
     For success_wo_mut this is the same program minimally repaired.
     For success_w_mut / fail it is structurally different but still correct.
  2. If parsing fails, fall back to the structurally closest correct file
     (Original Correct File Name in the CSV). Only used when a single file
     name is present (question_1 style); skipped for multi-function mappings.
  3. Last resort: reference.py.

Usage:
  python create_ground_truth.py --base-dir Data/question_1
  python create_ground_truth.py --base-dir Data/question_2
"""
from __future__ import annotations

import argparse
import ast
import csv
import difflib
import json
import re
from pathlib import Path



# ---------------------------------------------------------------------------
# CSV helpers
# ---------------------------------------------------------------------------

def load_csv(csv_file: Path) -> list[dict]:
    with csv_file.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_single_correct_filename(raw: str) -> str | None:
    """Extract correct filename only when there is exactly one function mapping."""
    matches = re.findall(r"'(correct_\d+_\d+\.py)'", raw)
    return matches[0] if len(matches) == 1 else None


# ---------------------------------------------------------------------------
# Line helpers
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


# ---------------------------------------------------------------------------
# Core diff
# ---------------------------------------------------------------------------

def find_buggy_lines(wrong_lines: list[str], correct_lines: list[str]) -> list[int]:
    norm_wrong = [normalize(l) for l in wrong_lines]
    norm_correct = [normalize(l) for l in correct_lines]

    matcher = difflib.SequenceMatcher(None, norm_wrong, norm_correct, autojunk=False)
    total_wrong = sum(1 for l in wrong_lines if l.strip())

    candidates: list[int] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            continue
        if tag in ('replace', 'delete'):
            block_size = i2 - i1
            # Skip large replace/delete blocks that indicate a full structural rewrite
            if total_wrong > 0 and block_size / total_wrong > 0.5:
                continue
            for i in range(i1, i2):
                if is_semantic(wrong_lines[i], in_diff=True):
                    candidates.append(i + 1)
        elif tag == 'insert':
            # Lines missing from wrong — point to the line just before the gap
            nearest = i1
            if nearest > 0 and is_semantic(wrong_lines[nearest - 1], in_diff=False):
                if nearest not in candidates:
                    candidates.append(nearest)

    if candidates:
        return candidates

    # Fallback: wrong is missing lines (omission bug).
    wrong_nonempty = sum(1 for l in wrong_lines if l.strip())
    correct_nonempty = sum(1 for l in correct_lines if l.strip())
    if wrong_nonempty < correct_nonempty:
        last = last_semantic_line(wrong_lines)
        if last:
            return [last]

    return []


# ---------------------------------------------------------------------------
# De-tokenize CSV code
# ---------------------------------------------------------------------------

def detokenize_to_lines(tokenized_code: str) -> list[str] | None:
    try:
        tree = ast.parse(tokenized_code)
        return ast.unparse(tree).splitlines()
    except SyntaxError:
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", required=True,
                        help="Path to question folder, e.g. Data/question_2")
    args = parser.parse_args()

    base = Path(args.base_dir)
    wrong_dir = base / "code" / "wrong"
    correct_dir = base / "code" / "correct"
    reference_file = base / "code" / "reference" / "reference.py"
    csv_file = base / "refactory_online.csv"
    output_file = base / "ground_truth.jsonl"

    rows = load_csv(csv_file)
    row_by_name = {r["File Name"].strip(): r for r in rows}
    reference_lines = reference_file.read_text(encoding="utf-8").splitlines()

    results: list[dict] = []
    stats = {"refactored": 0, "correct_file": 0, "reference": 0, "parse_fail": 0}

    for wrong_file in sorted(wrong_dir.glob("*.py")):
        wrong_name = wrong_file.name
        wrong_lines = wrong_file.read_text(encoding="utf-8").splitlines()
        row = row_by_name.get(wrong_name)

        correct_lines: list[str] | None = None

        # 1. Try Refactored Correct Code from CSV
        if row and row.get("Refactored Correct Code", "").strip():
            correct_lines = detokenize_to_lines(row["Refactored Correct Code"])
            if correct_lines is not None:
                stats["refactored"] += 1
            else:
                stats["parse_fail"] += 1

        # 2. Try matched correct file (only for single-function questions)
        if correct_lines is None and row:
            correct_name = parse_single_correct_filename(
                row.get("Original Correct File Name", "")
            )
            if correct_name:
                correct_file = correct_dir / correct_name
                if correct_file.exists():
                    correct_lines = correct_file.read_text(encoding="utf-8").splitlines()
                    stats["correct_file"] += 1

        # 3. Last resort: reference
        if correct_lines is None:
            correct_lines = reference_lines
            stats["reference"] += 1

        buggy = find_buggy_lines(wrong_lines, correct_lines)

        # If nothing was found, the program is likely incomplete (missing functions
        # or all present code is correct). Report the last semantic line as an
        # omission marker rather than leaving the entry empty.
        if not buggy:
            last = last_semantic_line(wrong_lines)
            if last:
                buggy = [last]

        results.append({"program_name": wrong_name, "buggy_lines": buggy})

    output_file.write_text(
        "\n".join(json.dumps(r) for r in results) + "\n",
        encoding="utf-8",
    )

    empty = sum(1 for r in results if not r["buggy_lines"])
    print(f"Wrote {len(results)} entries to {output_file}")
    print(f"  Used Refactored Correct Code: {stats['refactored']}")
    print(f"  Used matched correct file:    {stats['correct_file']}")
    print(f"  Used reference fallback:      {stats['reference']}")
    print(f"  Parse failures:               {stats['parse_fail']}")
    print(f"  Empty buggy_lines:            {empty}")
    print("\nSample output:")
    for r in results[:5]:
        print(" ", json.dumps(r))


if __name__ == "__main__":
    main()
