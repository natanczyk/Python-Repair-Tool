#!/usr/bin/env python3
"""
Build Data_QuixBugs/ from QuixBugs (one program = one injected bug), in the same
question_N layout as Data/ (Refactory), so faulty_lines_finder_refactory.py and
repair_research/run_repair.py run against it unmodified.

Ground truth is computed the same way as create_ground_truth.py: diff the buggy
code against the correct reference and report the changed/missing lines. Unlike
Refactory there is no CSV to consult — QuixBugs already ships the exact correct
version of every program (correct_python_programs/<name>.py), so that's used
directly as the reference for both the diff and Program.get_description().

Structure produced (one question per QuixBugs program, numbered alphabetically):
  Data_QuixBugs/
    manifest.json                      <- {"question_1": {"name": "bitcount", "has_tests": true}, ...}
    question_N/
      code/
        wrong/wrong_<name>.py          <- buggy version (+ node.py copy if the program needs it)
        reference/reference.py         <- correct version
      description.txt                  <- program's trailing docstring (task description)
      ground_truth.jsonl               <- {"program_name": "wrong_<name>.py", "buggy_lines": [...]}
      test_suite.py                    <- generated from json_testcases/<name>.json, or adapted
                                           from python_testcases/test_<name>.py for the 9
                                           graph/linked-list programs that have no JSON testdata
      ans/input_NNN.txt, output_NNN.txt  <- only for the 31 JSON-backed programs (the 9
                                             graph-based ones can't be reduced to a single-line
                                             call, so ranking/minimal_tests LLM modes will skip
                                             them; fauxpy and minimal_notests still work for all 40)

Usage:
  python prepare_quixbugs_data.py
"""
from __future__ import annotations

import ast
import difflib
import json
import re
import shutil
from pathlib import Path

QUIXBUGS_ROOT = Path("QuixBugs")
OUT_ROOT = Path("Data_QuixBugs")

# Programs with no json_testcases (graph / linked-list inputs) — test suites are
# adapted from the hand-written python_testcases/test_<name>.py instead.
GRAPH_PROGRAMS = {
    "breadth_first_search", "depth_first_search", "detect_cycle",
    "minimum_spanning_tree", "reverse_linked_list", "shortest_path_length",
    "shortest_path_lengths", "shortest_paths", "topological_ordering",
}
NEEDS_NODE = {
    "breadth_first_search", "depth_first_search", "detect_cycle",
    "reverse_linked_list", "shortest_path_length", "topological_ordering",
}


# ---------------------------------------------------------------------------
# Ground-truth diff (same approach as Faulty_Lines_and_Repair_research/create_ground_truth.py)
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
# Trailing-docstring extraction (QuixBugs programs end with a module-level
# string literal documenting the task — used as description.txt and excluded
# from the ground-truth diff since correct_python_programs/ doesn't have it).
# ---------------------------------------------------------------------------

def split_trailing_docstring(source: str) -> tuple[list[str], str | None]:
    lines = source.splitlines()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return lines, None

    if not tree.body:
        return lines, None
    last = tree.body[-1]
    if not (isinstance(last, ast.Expr) and isinstance(last.value, ast.Constant)
            and isinstance(last.value.value, str)):
        return lines, None

    code_lines = lines[: last.lineno - 1]
    return code_lines, last.value.value.strip()


# ---------------------------------------------------------------------------
# Test suite generation
# ---------------------------------------------------------------------------

def build_json_test_suite(name: str, testdata: list[tuple[list, object]]) -> tuple[str, list[tuple[str, str]]]:
    """Returns (test_suite.py contents, [(call_str, output_str), ...])."""
    lines = []
    pairs: list[tuple[str, str]] = []
    for i, (args, expected) in enumerate(testdata, 1):
        call_str = f"{name}({', '.join(repr(a) for a in args)})"
        # Some QuixBugs functions (e.g. flatten, kheapsort) return a generator
        # by design. Comparing an unconsumed generator to a list is always
        # false without ever executing the function body, which also means
        # FauxPy sees zero coverage to rank. Wrapping in list() when the
        # expected value is itself a list forces consumption either way --
        # a no-op for functions that already return a real list.
        actual = f"list({call_str})" if isinstance(expected, list) else call_str
        lines.append(f"def test_case{i:03d}():")
        lines.append(f"    assert {actual} == {expected!r}")
        lines.append("")
        pairs.append((call_str, str(expected)))
    return "\n".join(lines) + "\n", pairs


_GRAPH_TEST_STRIP_PATTERNS = (
    re.compile(r"^import pytest\s*$"),
    re.compile(r"^if pytest\.use_correct:\s*$"),
    re.compile(r"^\s*from correct_python_programs\."),
    re.compile(r"^else:\s*$"),
    re.compile(r"^\s*from python_programs\."),
)


def adapt_graph_test_suite(source: str) -> str:
    """Strips the QuixBugs pytest.use_correct import-switch boilerplate, keeping
    `from node import Node` and the bare test bodies (which already call the
    function under test by name, matching the conftest builtins-injection trick)."""
    out_lines = []
    for line in source.splitlines():
        if any(p.match(line) for p in _GRAPH_TEST_STRIP_PATTERNS):
            continue
        out_lines.append(line)
    # collapse the blank-line gaps left behind by the stripped block
    text = "\n".join(out_lines)
    text = re.sub(r"\n{3,}", "\n\n\n", text).strip("\n") + "\n"
    return text


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    buggy_dir = QUIXBUGS_ROOT / "python_programs"
    correct_dir = QUIXBUGS_ROOT / "correct_python_programs"
    json_dir = QUIXBUGS_ROOT / "json_testcases"
    graph_tests_dir = QUIXBUGS_ROOT / "python_testcases"
    node_py = QUIXBUGS_ROOT / "python_programs" / "node.py"

    names = sorted(
        p.stem for p in buggy_dir.glob("*.py")
        if p.stem != "node" and not p.stem.endswith("_test")
    )
    print(f"Found {len(names)} QuixBugs programs.")

    OUT_ROOT.mkdir(exist_ok=True)
    manifest: dict[str, dict] = {}

    stats = {"json_backed": 0, "graph_adapted": 0, "empty_ground_truth": 0}

    for idx, name in enumerate(names, 1):
        q_dir = OUT_ROOT / f"question_{idx}"
        wrong_dir = q_dir / "code" / "wrong"
        ref_dir = q_dir / "code" / "reference"
        wrong_dir.mkdir(parents=True, exist_ok=True)
        ref_dir.mkdir(parents=True, exist_ok=True)

        buggy_source = (buggy_dir / f"{name}.py").read_text(encoding="utf-8")
        correct_source = (correct_dir / f"{name}.py").read_text(encoding="utf-8")

        wrong_name = f"wrong_{name}.py"
        (wrong_dir / wrong_name).write_text(buggy_source, encoding="utf-8")
        (ref_dir / "reference.py").write_text(correct_source, encoding="utf-8")

        if name in NEEDS_NODE:
            shutil.copy(node_py, wrong_dir / "node.py")

        # description.txt from the trailing docstring
        wrong_code_lines, description = split_trailing_docstring(buggy_source)
        correct_code_lines, _ = split_trailing_docstring(correct_source)
        (q_dir / "description.txt").write_text(description or "", encoding="utf-8")

        # ground_truth.jsonl
        buggy_lines = find_buggy_lines(wrong_code_lines, correct_code_lines)
        if not buggy_lines:
            stats["empty_ground_truth"] += 1
        (q_dir / "ground_truth.jsonl").write_text(
            json.dumps({"program_name": wrong_name, "buggy_lines": buggy_lines}) + "\n",
            encoding="utf-8",
        )

        # test_suite.py (+ ans/ where possible)
        json_file = json_dir / f"{name}.json"
        if name not in GRAPH_PROGRAMS and json_file.exists():
            testdata = [json.loads(line) for line in json_file.read_text(encoding="utf-8").splitlines() if line.strip()]
            content, pairs = build_json_test_suite(name, testdata)
            (q_dir / "test_suite.py").write_text(content, encoding="utf-8")

            ans_dir = q_dir / "ans"
            ans_dir.mkdir(exist_ok=True)
            for i, (call_str, out_str) in enumerate(pairs, 1):
                (ans_dir / f"input_{i:03d}.txt").write_text(call_str, encoding="utf-8")
                (ans_dir / f"output_{i:03d}.txt").write_text(out_str, encoding="utf-8")
            stats["json_backed"] += 1
            manifest[f"question_{idx}"] = {"name": name, "has_tests": True, "kind": "json"}
        else:
            graph_test_file = graph_tests_dir / f"test_{name}.py"
            if graph_test_file.exists():
                adapted = adapt_graph_test_suite(graph_test_file.read_text(encoding="utf-8"))
                (q_dir / "test_suite.py").write_text(adapted, encoding="utf-8")
                stats["graph_adapted"] += 1
                manifest[f"question_{idx}"] = {"name": name, "has_tests": True, "kind": "graph"}
            else:
                print(f"  [warn] {name}: no json_testcases and no python_testcases/test_{name}.py found")
                manifest[f"question_{idx}"] = {"name": name, "has_tests": False, "kind": "none"}

        print(f"  question_{idx:>2} = {name}  (buggy_lines={buggy_lines})")

    (OUT_ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nDone. {len(names)} questions written to {OUT_ROOT}/")
    print(f"  JSON-backed test suites (with ans/):        {stats['json_backed']}")
    print(f"  Graph/linked-list adapted test suites:      {stats['graph_adapted']}")
    print(f"  Empty ground truth (no diff found):         {stats['empty_ground_truth']}")


if __name__ == "__main__":
    main()