"""
Table 9. How invasive are Refactory repairs? -- direct parallel to
quix_repair/table9_invasiveness.py.

For every solved-and-saved repaired submission in
repaired_versions/refactory/<type>_<model>/, measures how much the repair
actually changed relative to the *original buggy submission* (not a
reference solution -- see quix_repair's version for the full reasoning),
and compares that to the submission's own ground-truth bug-set size.

This deliberately avoids diffing against reference.py: Refactory's
create_ground_truth.py picks a *different* correct-code source per
submission (the student's own de-tokenized "Refactored Correct Code" from
the CSV first, a matched correct/ file second, reference.py only as a last
resort) -- so comparing every repaired file against the single shared
reference.py, as an earlier version of this script did, systematically
inflates the measured distance for any submission whose true closest-
correct-code wasn't reference.py itself (confirmed: doing so put the mean
buggy-vs-reference distance at ~8 lines against a mean ground-truth bug
size of ~2.6 -- a ~3x gap that has nothing to do with actual invasiveness).
Diffing repaired-vs-buggy instead sidesteps this source-selection problem
entirely, since both files are unambiguous and already on disk.

Unlike QuixBugs, Refactory submission filenames already encode the
question number directly (wrong_<question>_<index>.py), so no manifest
lookup is needed. Only whichever (type, model) folders actually exist
under repaired_versions/refactory/ are processed -- as of writing, only
best_loc has been downloaded for all 8 models.
"""
from __future__ import annotations

import ast
import re

import numpy as np
import pandas as pd

from common import (
    ROOT, DATA_ROOT, OUT_TABLES, MODELS, TYPES, MODEL_LABELS, TYPE_LABELS,
    load_ground_truth_sizes,
)

REPAIRED_ROOT = ROOT / "repaired_versions" / "refactory"

_QUESTION_RE = re.compile(r"^wrong_(\d+)_\d+\.py$")


def question_of(filename: str) -> int | None:
    m = _QUESTION_RE.match(filename)
    return int(m.group(1)) if m else None


def strip_trailing_string_statement(source: str) -> str:
    """Drops a trailing bare string-literal statement, if any -- kept
    defensively in case any student submissions or repaired outputs carry
    a trailing docstring/comment block the other side of the pair lacks
    (same issue confirmed on QuixBugs; not verified at scale for Refactory,
    but harmless if absent)."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return source
    if not tree.body:
        return source
    last = tree.body[-1]
    if not (isinstance(last, ast.Expr) and isinstance(last.value, ast.Constant)
            and isinstance(last.value.value, str)):
        return source
    lines = source.splitlines()
    return "\n".join(lines[: last.lineno - 1])


def normalize(line: str) -> str:
    rstripped = line.rstrip()
    indent = len(rstripped) - len(rstripped.lstrip())
    content = re.sub(r" {2,}", " ", rstripped.strip())
    return " " * indent + content


def diff_metrics(a_text: str, b_text: str) -> tuple[int, float]:
    """Returns (lines_changed, similarity_ratio) between two code texts,
    after stripping any trailing bare string-literal statement from both."""
    import difflib
    a_text = strip_trailing_string_statement(a_text)
    b_text = strip_trailing_string_statement(b_text)
    a_lines = [normalize(l) for l in a_text.splitlines()]
    b_lines = [normalize(l) for l in b_text.splitlines()]
    matcher = difflib.SequenceMatcher(None, a_lines, b_lines, autojunk=False)

    changed = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        changed += max(i2 - i1, j2 - j1)

    ratio = matcher.ratio()
    return changed, ratio


def build_table9() -> pd.DataFrame:
    gt_sizes = load_ground_truth_sizes()  # {(question, "wrong_N_XXX.py"): n_buggy_lines}

    rows = []
    for t in TYPES:
        for model in MODELS:
            d = REPAIRED_ROOT / f"{t}_{model}"
            if not d.exists():
                continue

            changes, ratios, gt_ns = [], [], []
            for f in sorted(d.glob("*.py")):
                q = question_of(f.name)
                if q is None:
                    continue
                wrong_path = DATA_ROOT / f"question_{q}" / "code" / "wrong" / f.name
                if not wrong_path.exists():
                    continue

                repaired_text = f.read_text(encoding="utf-8")
                buggy_text = wrong_path.read_text(encoding="utf-8")

                changed, ratio = diff_metrics(repaired_text, buggy_text)
                changes.append(changed)
                ratios.append(ratio)
                gt_ns.append(gt_sizes.get((q, f.name), np.nan))

            if not changes:
                continue

            mean_changed = np.mean(changes)
            mean_gt = np.nanmean(gt_ns)

            rows.append({
                "Model": MODEL_LABELS[model],
                "Type": TYPE_LABELS[t],
                "n solved": len(changes),
                "Mean lines changed (repaired vs buggy)": mean_changed,
                "Mean similarity": np.mean(ratios),
                "Mean GT bug size": mean_gt,
                "Invasiveness ratio (changed / GT size)": mean_changed / mean_gt,
            })

    return pd.DataFrame(rows).set_index(["Model", "Type"])


if __name__ == "__main__":
    table9 = build_table9().round(3)
    print("Invasiveness of Refactory repairs: repaired file vs. original buggy submission")
    print("(solved-and-saved submissions only; see module docstring for methodology)\n")
    print(table9.to_string())

    csv_path = OUT_TABLES / "table9_invasiveness.csv"
    table9.to_csv(csv_path)
    print(f"\n[saved] {csv_path}")