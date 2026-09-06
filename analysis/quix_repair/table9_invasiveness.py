"""
Table 9. How invasive are QuixBugs repairs?

For every solved-and-saved repaired submission in repaired_versions/<type>_<model>/,
measures how much the repair actually changed relative to the *original
buggy submission* (not a reference solution -- see below for why), and
compares that to how much change the bug's own ground truth says was
required. A model that solves fewer submissions but changes close to the
minimal number of lines is doing something qualitatively different from
one that solves more by rewriting much more of the file than necessary --
solve rate alone (Table 1) can't tell these apart.

Deliberately NOT diffed against reference.py: since every file here is
already a solved, test-passing submission, correctness isn't in question,
so "how close does it land to one specific canonical implementation" adds
noise without adding information (QuixBugs' reference.py files can also
carry unrelated trailing content inherited from the upstream benchmark,
which would have to be stripped out first). Diffing repaired-vs-buggy
directly is simpler, avoids that noise entirely, and is arguably a more
direct definition of "invasiveness" anyway: how much of the original code
did the model actually touch.

Distance is computed the same way ground truth itself is constructed
elsewhere in this project: difflib.SequenceMatcher over whitespace-
normalized lines.
"""
from __future__ import annotations

import ast
import re

import numpy as np
import pandas as pd

from common import (
    ROOT, DATA_ROOT, OUT_TABLES, MODELS, TYPES, MODEL_LABELS, TYPE_LABELS,
    load_ground_truth_sizes, _question_lookup,
)

REPAIRED_ROOT = ROOT / "repaired_versions"


def strip_trailing_string_statement(source: str) -> str:
    """Drops a trailing bare string-literal statement, if any. QuixBugs'
    buggy files end with a documentation docstring (name, input/output
    contract, examples); repair prompts ask the model to "return ONLY the
    corrected code", so most repaired files simply omit it. Comparing the
    two directly would otherwise count that dropped documentation as a
    ~10-13 line "change" that has nothing to do with the actual fix."""
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
    q_lookup = _question_lookup()  # {"wrong_<name>.py": question_N}
    gt_sizes = load_ground_truth_sizes()  # {(question, "wrong_<name>.py"): n_buggy_lines}

    rows = []
    for t in TYPES:
        for model in MODELS:
            d = REPAIRED_ROOT / f"{t}_{model}"
            if not d.exists():
                continue

            changes, ratios, gt_ns = [], [], []
            for f in sorted(d.glob("*.py")):
                q = q_lookup.get(f.name)
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
    print("Invasiveness of QuixBugs repairs: repaired file vs. original buggy submission")
    print("(solved-and-saved submissions only; see module docstring for methodology)\n")
    print(table9.to_string())

    csv_path = OUT_TABLES / "table9_invasiveness.csv"
    table9.to_csv(csv_path)
    print(f"\n[saved] {csv_path}")