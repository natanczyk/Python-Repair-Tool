#!/usr/bin/env python3
"""
Build Data_Bench from DebugBench (HuggingFace: Rtian/DebugBench).
Filters to Python submissions, groups by difficulty level.

Structure produced:
  Data_Bench/
    question_easy/
      code/
        wrong/wrong_easy_001.py          <- buggy_code
        reference/reference_easy_001.py  <- solution (matched by index to wrong)
      ans/wrong_easy_001/
        input_001.txt                    <- parsed from examples field
        output_001.txt
      metadata.jsonl                     <- slug, category, subtype per submission
    question_medium/
    question_hard/
    Descriptions/
      wrong_easy_001_description.txt     <- question + constraints + examples
    test_suites/
      test_easy_001.py                   <- pytest (best-effort from examples)
"""

import ast
import importlib.util
import json
import os
import re
import ssl
from pathlib import Path

# Disable SSL verification for corporate/institutional networks
ssl._create_default_https_context = ssl._create_unverified_context
os.environ["CURL_CA_BUNDLE"] = ""
os.environ["REQUESTS_CA_BUNDLE"] = ""

import pandas as pd

ROOT = Path("Data_Bench")
LEVELS = ("easy", "medium", "hard")


def load_dataset() -> pd.DataFrame:
    print("Loading DebugBench from HuggingFace...")
    df = pd.read_json("hf://datasets/Rtian/DebugBench/eval.json")
    print(f"  Total rows: {len(df)}")
    print(f"  Columns: {df.columns.tolist()}")
    if "language" in df.columns:
        print(f"  Language values: {df['language'].unique().tolist()}")
    if "level" in df.columns:
        print(f"  Level values: {df['level'].unique().tolist()}")
    df = df[df["language"] == "python3"].reset_index(drop=True)
    print(f"  {len(df)} python3 rows after filter")
    return df


def parse_examples(examples) -> list[tuple[str, str]]:
    """Return list of (input_str, output_str) from LeetCode example strings."""
    if not examples:
        return []
    pairs = []
    for ex in examples:
        ex = str(ex)
        inp = re.search(r"Input:\s*(.*?)(?=\nOutput:)", ex, re.DOTALL | re.IGNORECASE)
        out = re.search(r"Output:\s*(.*?)(?=\nExplanation:|\nExample|\Z)", ex, re.DOTALL | re.IGNORECASE)
        if inp and out:
            pairs.append((inp.group(1).strip(), out.group(1).strip()))
    return pairs


def get_solution_method(code: str) -> tuple[str | None, list[str]]:
    """Extract first public method name + params from class Solution."""
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "Solution":
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and not item.name.startswith("_"):
                        params = [a.arg for a in item.args.args if a.arg != "self"]
                        return item.name, params
    except Exception:
        pass
    return None, []


def build_test_case(method: str, params: list[str], input_str: str, output_str: str, idx: int) -> str:
    param_vals: dict[str, str] = {}
    for part in re.split(r",\s*(?=[a-zA-Z_]\w*\s*=)", input_str):
        m = re.match(r"([a-zA-Z_]\w*)\s*=\s*(.*)", part.strip())
        if m:
            param_vals[m.group(1)] = m.group(2).strip()

    args = [param_vals[p] for p in params if p in param_vals]
    if len(args) != len(params):
        return f"# test_case_{idx}: could not parse inputs (complex/missing params)\n\n"
    args_str = ", ".join(args)
    return (
        f"def test_case_{idx}():\n"
        f"    sol = Solution()\n"
        f"    result = sol.{method}({args_str})\n"
        f"    assert result == {output_str}\n\n"
    )


def build_test_file(name: str, level: str, method: str, params: list[str],
                    pairs: list[tuple[str, str]], slug: str) -> str:
    lines = [
        f"# Auto-generated test for {name}  (slug: {slug})\n",
        "import importlib.util, pathlib\n\n",
        "_wrong_path = (\n",
        f"    pathlib.Path(__file__).parent.parent\n",
        f"    / 'question_{level}' / 'code' / 'wrong' / '{name}.py'\n",
        ")\n",
        "_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)\n",
        "_mod = importlib.util.module_from_spec(_spec)\n",
        "_spec.loader.exec_module(_mod)\n",
        "Solution = _mod.Solution\n\n",
    ]
    for t_idx, (inp, out) in enumerate(pairs, 1):
        lines.append(build_test_case(method, params, inp, out, t_idx))
    return "".join(lines)


def make_description(row: pd.Series) -> str:
    parts = []
    if row.get("question"):
        parts.append(str(row["question"]))
    if row.get("constraints"):
        parts.append(f"\nConstraints:\n{row['constraints']}")
    if row.get("examples"):
        ex_text = "\n".join(str(e) for e in row["examples"])
        parts.append(f"\nExamples:\n{ex_text}")
    return "\n".join(parts)


def build_dataset(df: pd.DataFrame) -> None:
    ROOT.mkdir(exist_ok=True)
    (ROOT / "Descriptions").mkdir(exist_ok=True)
    (ROOT / "test_suites").mkdir(exist_ok=True)

    totals: dict[str, int] = {lvl: 0 for lvl in LEVELS}
    skipped_tests = 0

    for level in LEVELS:
        group = df[df["level"] == level]
        if group.empty:
            continue

        q_dir = ROOT / f"question_{level}"
        (q_dir / "code" / "wrong").mkdir(parents=True, exist_ok=True)
        (q_dir / "code" / "reference").mkdir(parents=True, exist_ok=True)
        (q_dir / "ans").mkdir(exist_ok=True)

        meta_rows: list[dict] = []

        for _, row in group.iterrows():
            idx = totals[level] + 1
            totals[level] += 1

            name = f"wrong_{level}_{idx:03d}"
            ref_name = f"reference_{level}_{idx:03d}"

            buggy_code: str = row.get("buggy_code") or ""
            solution: str = row.get("solution") or ""
            slug: str = row.get("slug") or ""

            # Wrong submission and its matching reference
            (q_dir / "code" / "wrong" / f"{name}.py").write_text(buggy_code, encoding="utf-8")
            (q_dir / "code" / "reference" / f"{ref_name}.py").write_text(solution, encoding="utf-8")

            # Metadata (lightweight — maps wrong → reference + DebugBench fields)
            meta_rows.append({
                "program_name": f"{name}.py",
                "reference_name": f"{ref_name}.py",
                "slug": slug,
                "category": row.get("category") or "",
                "subtype": row.get("subtype") or "",
            })

            # I/O pairs parsed from examples
            pairs = parse_examples(row.get("examples") or [])
            if pairs:
                ans_dir = q_dir / "ans" / name
                ans_dir.mkdir(exist_ok=True)
                for t_idx, (inp, out) in enumerate(pairs, 1):
                    (ans_dir / f"input_{t_idx:03d}.txt").write_text(inp, encoding="utf-8")
                    (ans_dir / f"output_{t_idx:03d}.txt").write_text(out, encoding="utf-8")

            # Description
            (ROOT / "Descriptions" / f"{name}_description.txt").write_text(
                make_description(row), encoding="utf-8"
            )

            # Test suite (best effort from examples)
            method, params = get_solution_method(solution or buggy_code)
            if method and pairs:
                content = build_test_file(name, level, method, params, pairs, slug)
                (ROOT / "test_suites" / f"test_{name}.py").write_text(content, encoding="utf-8")
            else:
                skipped_tests += 1

        with open(q_dir / "metadata.jsonl", "w", encoding="utf-8") as f:
            for m in meta_rows:
                f.write(json.dumps(m) + "\n")

        print(f"  question_{level}: {totals[level]} submissions")

    total = sum(totals.values())
    print(f"\nDone. Data_Bench/ created with {total} Python submissions.")
    for lvl in LEVELS:
        print(f"  {lvl}: {totals[lvl]}")
    if skipped_tests:
        print(f"  Test suites skipped (no parseable method/examples): {skipped_tests}")


if __name__ == "__main__":
    df = load_dataset()
    build_dataset(df)
