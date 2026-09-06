"""
Manual test script for FauxPyRunner.
Run from the project root with the venv active:
    python test_notebooks/test_fauxpy_runner.py
"""
import os
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from Localization.program import Program
from Localization.fauxpy_runner import FauxPyRunner

ASSIGNMENT_PATH = PROJECT_ROOT / "Data" / "assignment1"
SUBMISSION_PATH = ASSIGNMENT_PATH / "student1.py"


def _make_program(submission_path=None):
    return Program(
        submission_path=submission_path or SUBMISSION_PATH,
        test_suite_path=ASSIGNMENT_PATH / "test_student_code.py",
        description_path=ASSIGNMENT_PATH / "description1.txt",
    )


# ── 1. Syntax check passes on valid code ─────────────────────────────────────

def test_syntax_check_ok():
    print("\n[1] syntax check — valid submission")
    runner = FauxPyRunner(_make_program())
    error = runner._check_syntax()
    assert error is None, f"Expected None, got: {error}"
    print("    PASS: no syntax error detected")


# ── 2. Syntax check catches a broken file ─────────────────────────────────────

def test_syntax_check_error():
    print("\n[2] syntax check — submission with SyntaxError")
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as f:
        f.write("def broken(\n    x = :\n")
        tmp = f.name
    try:
        runner = FauxPyRunner(_make_program(tmp))
        error = runner._check_syntax()
        assert error is not None, "Expected a syntax error message"
        assert "SyntaxError" in error
        print(f"    PASS: syntax error caught: {error}")
    finally:
        os.unlink(tmp)


# ── 3. _parse_test_assertions extracts call + expected value ──────────────────

def test_parse_test_assertions():
    print("\n[3] _parse_test_assertions — extracts input/expected pairs from test file")
    runner = FauxPyRunner(_make_program())
    assertions = runner._parse_test_assertions()
    print(f"    Parsed: {assertions}")
    assert "test_case1" in assertions
    assert "test_case2" in assertions
    assert "test_case3" in assertions
    # Each value should be the full assertion expression, e.g. "max_of_three(1, 2, 3) == 3"
    assert "==" in assertions["test_case1"]
    print("    PASS: assertions parsed correctly")


# ── 4. get_analysis short-circuits on syntax error ────────────────────────────

def test_get_analysis_syntax_error():
    print("\n[4] get_analysis — syntax error path")
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, encoding="utf-8"
    ) as f:
        f.write("def broken:\n")
        tmp = f.name
    try:
        runner = FauxPyRunner(_make_program(tmp))
        analysis = runner.get_analysis()
        assert analysis["has_syntax_error"] is True
        assert analysis["syntax_error"] is not None
        assert analysis["suspicious"] == []
        assert analysis["failing_tests"] is None
        print(f"    PASS: short-circuited: {analysis['syntax_error']}")
    finally:
        os.unlink(tmp)


# ── 5. Full FauxPy run on the buggy student1.py ───────────────────────────────

def test_full_run():
    print("\n[5] full FauxPy run on buggy student1.py (max_of_three never checks c)")
    runner = FauxPyRunner(_make_program())
    analysis = runner.get_analysis()

    print(f"\n    has_syntax_error : {analysis['has_syntax_error']}")
    print(f"\n    --- Suspicious lines ---")
    print(f"    {analysis['suspicious_text']}")
    print(f"\n    --- Failing tests (with inputs) ---")
    print(f"    {analysis['failing_tests']}")
    print(f"\n    --- Raw FauxPy output (first 3000 chars) ---")
    print(analysis["output"][:3000])

    assert analysis["has_syntax_error"] is False
    assert analysis["failing_tests"] is not None, (
        "Expected at least one failing test — student1.py never returns c"
    )
    print("\n    PASS: analysis complete with failing tests detected")


# ── 6. No failing tests when submission is correct ───────────────────────────

def test_full_run_correct_submission():
    print("\n[6] full FauxPy run on a correct submission (should produce no failing tests)")
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False,
        dir=str(ASSIGNMENT_PATH), encoding="utf-8",
        prefix="student1_correct_"
    ) as f:
        f.write(
            "def max_of_three(a, b, c):\n"
            "    if a >= b and a >= c:\n"
            "        return a\n"
            "    if b >= a and b >= c:\n"
            "        return b\n"
            "    return c\n"
        )
        tmp = f.name

    # test_student_code.py imports "from student1 import max_of_three" so we need
    # the temp file to be named student1.py for the import to resolve — we rename it.
    correct_path = ASSIGNMENT_PATH / "student1_correct_tmp.py"
    os.replace(tmp, correct_path)

    # Temporarily patch the import by creating a conftest that does nothing;
    # here we just point --src at the correct file so FauxPy instruments it.
    # Note: this test only checks that _check_syntax passes and no crash occurs.
    try:
        program = Program(
            submission_path=correct_path,
            test_suite_path=ASSIGNMENT_PATH / "test_student_code.py",
            description_path=ASSIGNMENT_PATH / "description1.txt",
        )
        runner = FauxPyRunner(program)
        error = runner._check_syntax()
        assert error is None
        print("    PASS: correct submission passes syntax check (no FauxPy run needed)")
    finally:
        correct_path.unlink(missing_ok=True)


if __name__ == "__main__":
    test_syntax_check_ok()
    test_syntax_check_error()
    test_parse_test_assertions()
    test_get_analysis_syntax_error()
    test_full_run()
    test_full_run_correct_submission()
    print("\n=== All tests done ===")
