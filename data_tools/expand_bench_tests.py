#!/usr/bin/env python3
"""
Expand Data_Bench test suites to up to TARGET test cases per submission.

- Simple types (int, str, list[int], etc.): generates variations, runs against
  reference to get expected outputs, writes up to TARGET verified test cases.
- Complex types (TreeNode, ListNode): keeps existing examples but fixes syntax.
- Fixes false/true/null → False/True/None in all test files.
"""

import ast
import concurrent.futures
import importlib.util
import inspect
import json
import re
import sys
from pathlib import Path

DATA_BENCH = Path("Data_Bench")
LEVELS = ("easy", "medium", "hard")
TARGET = 15
RUN_TIMEOUT = 3  # seconds per test case execution


# ---------------------------------------------------------------------------
# LeetCode literal conversion
# ---------------------------------------------------------------------------

def lc_to_py(s: str) -> str:
    """Convert LeetCode JSON-style literal to Python literal string."""
    s = s.strip()
    s = re.sub(r"\bnull\b", "None", s)
    s = re.sub(r"\btrue\b", "True", s)
    s = re.sub(r"\bfalse\b", "False", s)
    return s


def safe_literal(s: str):
    """Parse a Python literal string; return (value, ok)."""
    try:
        return ast.literal_eval(lc_to_py(s)), True
    except Exception:
        return None, False


# ---------------------------------------------------------------------------
# Reference solution loading
# ---------------------------------------------------------------------------

def load_reference(ref_path: Path):
    """Import reference solution module; return module or None."""
    from typing import List, Optional, Dict, Tuple, Set, Any, Union
    from collections import Counter, defaultdict, deque, OrderedDict
    import math, heapq, bisect, itertools, functools, operator

    spec = importlib.util.spec_from_file_location("_ref", ref_path)
    mod = importlib.util.module_from_spec(spec)
    # Pre-inject LeetCode globals (solutions use these without importing)
    mod.__dict__.update({
        "List": List, "Optional": Optional, "Dict": Dict, "Tuple": Tuple,
        "Set": Set, "Any": Any, "Union": Union,
        "Counter": Counter, "defaultdict": defaultdict, "deque": deque,
        "OrderedDict": OrderedDict,
        "math": math, "heapq": heapq, "bisect": bisect,
        "itertools": itertools, "functools": functools, "operator": operator,
    })
    try:
        spec.loader.exec_module(mod)
        return mod
    except Exception:
        return None


def get_method(mod) -> tuple[str | None, list[str]]:
    """Return (method_name, [param_names]) from Solution class."""
    if not hasattr(mod, "Solution"):
        return None, []
    for name, fn in inspect.getmembers(mod.Solution, predicate=inspect.isfunction):
        if not name.startswith("_"):
            params = [p for p in inspect.signature(fn).parameters if p != "self"]
            return name, params
    return None, []


# ---------------------------------------------------------------------------
# Complex-type detection
# ---------------------------------------------------------------------------

def is_complex(ref_path: Path, ans_dir: Path) -> bool:
    """True if problem uses TreeNode/ListNode or tree-array inputs."""
    code = ref_path.read_text(encoding="utf-8")
    if "TreeNode" in code or "ListNode" in code:
        return True
    for inp in ans_dir.glob("input_*.txt"):
        if "null" in inp.read_text(encoding="utf-8").lower():
            return True
    return False


# ---------------------------------------------------------------------------
# Input parsing from ans/ folder
# ---------------------------------------------------------------------------

def parse_input_file(text: str, params: list[str]) -> dict | None:
    """Parse 'k = 2, nums = [1,2]' into {param: value} dict."""
    text = lc_to_py(text.strip())
    vals: dict = {}
    for part in re.split(r",\s*(?=[a-zA-Z_]\w*\s*=)", text):
        m = re.match(r"([a-zA-Z_]\w*)\s*=\s*(.*)", part.strip(), re.DOTALL)
        if m:
            v, ok = safe_literal(m.group(2).strip())
            if ok:
                vals[m.group(1)] = v
    if all(p in vals for p in params):
        return vals
    return None


def load_existing_cases(ans_dir: Path, name: str, params: list[str]) -> list[dict]:
    sub_dir = ans_dir / name
    if not sub_dir.exists():
        return []
    cases = []
    for inp_file in sorted(sub_dir.glob("input_*.txt")):
        idx = inp_file.stem.replace("input_", "")
        out_file = sub_dir / f"output_{idx}.txt"
        if not out_file.exists():
            continue
        parsed = parse_input_file(inp_file.read_text(encoding="utf-8"), params)
        out_raw = out_file.read_text(encoding="utf-8").strip()
        out_val, ok = safe_literal(out_raw)
        if parsed and ok:
            cases.append({"inputs": parsed, "output": out_val})
    return cases


# ---------------------------------------------------------------------------
# Variation generation
# ---------------------------------------------------------------------------

def _int_vars(v: int) -> list:
    return list({0, 1, -1, v, v + 1, v - 1, v * 2, abs(v) + 10})


def _str_vars(v: str) -> list:
    base = ["", "a", "z", v[::-1], v + "a", "a" * max(1, len(v))]
    return list(dict.fromkeys(base))  # preserve order, dedupe


def _list_int_vars(v: list) -> list:
    safe = v if v else [1]
    candidates = [
        [],
        [safe[0]],
        sorted(safe),
        sorted(safe, reverse=True),
        list(reversed(safe)),
        safe + [0],
        [0] * max(1, len(safe)),
        [1] * max(1, len(safe)),
        [x + 1 for x in safe],
        [x - 1 for x in safe],
        safe * 2,
        list(set(safe)),
    ]
    seen, out = set(), []
    for c in candidates:
        key = tuple(c)
        if key not in seen:
            seen.add(key)
            out.append(c)
    return out


def _list_str_vars(v: list) -> list:
    safe = v if v else ["a"]
    return [[], [safe[0]], sorted(safe), list(reversed(safe)), safe + ["x"]]


def _list_list_int_vars(v: list) -> list:
    if not v or not v[0]:
        return [[[1]], [[0, 1], [1, 0]]]
    rows, cols = len(v), len(v[0])
    return [
        [[0] * cols for _ in range(rows)],
        [[1] * cols for _ in range(rows)],
        [list(reversed(r)) for r in v],
        list(reversed(v)),
    ]


def generate_param_variations(val) -> list:
    if isinstance(val, bool):
        return [True, False]
    if isinstance(val, int):
        return _int_vars(val)
    if isinstance(val, float):
        return [0.0, 1.0, -1.0, val, val * 2]
    if isinstance(val, str):
        return _str_vars(val)
    if isinstance(val, list):
        if not val:
            return [[], [0], [1], [1, 2]]
        if all(isinstance(x, int) and not isinstance(x, bool) for x in val):
            return _list_int_vars(val)
        if all(isinstance(x, str) for x in val):
            return _list_str_vars(val)
        if all(isinstance(x, list) for x in val):
            return _list_list_int_vars(val)
    return [val]


def generate_candidate_inputs(existing_cases: list[dict], params: list[str]) -> list[dict]:
    """Generate varied input dicts based on existing cases."""
    if not existing_cases:
        return []
    candidates = []
    for base_case in existing_cases:
        base = base_case["inputs"]
        for p in params:
            if p not in base:
                continue
            for var in generate_param_variations(base[p]):
                new = dict(base)
                new[p] = var
                candidates.append(new)
    return candidates


# ---------------------------------------------------------------------------
# Running against reference
# ---------------------------------------------------------------------------

def run_one(mod, method_name: str, inputs: dict, params: list[str]):
    """Run Solution().method(*ordered_args); return (result, ok)."""
    args = [inputs[p] for p in params]
    try:
        sol = mod.Solution()
        result = getattr(sol, method_name)(*args)
        return result, True
    except Exception:
        return None, False


def verify_cases(mod, method_name: str, candidates: list[dict],
                 params: list[str], target: int) -> list[dict]:
    """Run candidates against reference; return up to target verified (inputs, output) dicts."""
    verified = []
    seen_outputs = set()

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
        for inp in candidates:
            if len(verified) >= target:
                break
            future = ex.submit(run_one, mod, method_name, inp, params)
            try:
                result, ok = future.result(timeout=RUN_TIMEOUT)
            except Exception:
                continue
            if ok:
                out_key = repr(result)
                verified.append({"inputs": inp, "output": result})
                seen_outputs.add(out_key)
    return verified


# ---------------------------------------------------------------------------
# Test file writing
# ---------------------------------------------------------------------------

def _fmt(val) -> str:
    return repr(val)


def build_test_file(name: str, level: str, method: str, params: list[str],
                    cases: list[dict], slug: str) -> str:
    lines = [
        f"# Test suite for {name}  (slug: {slug})\n",
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
    for i, case in enumerate(cases, 1):
        args_str = ", ".join(_fmt(case["inputs"][p]) for p in params)
        lines.append(
            f"def test_case_{i}():\n"
            f"    sol = Solution()\n"
            f"    assert sol.{method}({args_str}) == {_fmt(case['output'])}\n\n"
        )
    return "".join(lines)


def fix_existing_test_file(path: Path) -> None:
    """Fix false/true/null literals in an existing test file in-place."""
    text = path.read_text(encoding="utf-8")
    fixed = re.sub(r"\bfalse\b", "False", text)
    fixed = re.sub(r"\btrue\b", "True", fixed)
    fixed = re.sub(r"\bnull\b", "None", fixed)
    if fixed != text:
        path.write_text(fixed, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_level(level: str) -> None:
    q_dir = DATA_BENCH / f"question_{level}"
    meta_path = q_dir / "metadata.jsonl"
    ts_dir = DATA_BENCH / "test_suites"
    ans_dir = q_dir / "ans"

    if not meta_path.exists():
        return

    meta = [json.loads(l) for l in meta_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    expanded = skipped_complex = fixed_only = errors = 0

    for m in meta:
        name = Path(m["program_name"]).stem        # wrong_easy_001
        ref_path = q_dir / "code" / "reference" / m["reference_name"]
        test_path = ts_dir / f"test_{name}.py"

        if not ref_path.exists():
            errors += 1
            continue

        # Only expand files that currently have exactly 2 or 3 test cases
        if test_path.exists():
            current_count = test_path.read_text(encoding="utf-8").count("def test_case_")
            if current_count not in (2, 3):
                continue

        def process_one(ref_path, test_path, ans_dir, name, slug):
            if is_complex(ref_path, ans_dir):
                if test_path.exists():
                    fix_existing_test_file(test_path)
                return "complex"

            mod = load_reference(ref_path)
            if mod is None:
                if test_path.exists():
                    fix_existing_test_file(test_path)
                return "error"

            method, params = get_method(mod)
            if not method or not params:
                if test_path.exists():
                    fix_existing_test_file(test_path)
                return "error"

            existing = load_existing_cases(ans_dir, name, params)
            if not existing:
                if test_path.exists():
                    fix_existing_test_file(test_path)
                return "fixed"

            if len(existing) >= TARGET:
                if test_path.exists():
                    fix_existing_test_file(test_path)
                return "fixed"

            candidates = [e["inputs"] for e in existing]
            candidates.extend(generate_candidate_inputs(existing, params))
            all_cases = verify_cases(mod, method, candidates, params, TARGET)

            content = build_test_file(name, level, method, params, all_cases, slug)
            test_path.write_text(content, encoding="utf-8")
            return "expanded"

        import concurrent.futures as _cf
        _ex = _cf.ThreadPoolExecutor(max_workers=1)
        try:
            _fut = _ex.submit(process_one, ref_path, test_path, ans_dir,
                              name, m.get("slug", ""))
            result = _fut.result(timeout=10)
        except Exception:
            if test_path.exists():
                fix_existing_test_file(test_path)
            errors += 1
            result = None
        finally:
            _ex.shutdown(wait=False)  # don't block on stuck threads

        if result == "complex":
            skipped_complex += 1
        elif result == "error":
            errors += 1
        elif result == "fixed":
            fixed_only += 1
        elif result == "expanded":
            expanded += 1
            if expanded % 50 == 0:
                print(f"  [{level}] {expanded} expanded so far...")

    print(f"  {level}: expanded={expanded}, complex_fixed={skipped_complex}, "
          f"fixed_only={fixed_only}, errors={errors}")


def main() -> None:
    print("Expanding Data_Bench test suites...")
    for level in LEVELS:
        print(f"\n[{level}]")
        process_level(level)
    print("\nDone.")


if __name__ == "__main__":
    main()
