# Test suite for wrong_medium_004  (slug: sequential-digits)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_004.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.sequentialDigits(100, 300) == [123, 234]

def test_case_2():
    sol = Solution()
    assert sol.sequentialDigits(1000, 13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345]

def test_case_3():
    sol = Solution()
    assert sol.sequentialDigits(0, 300) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 34, 45, 56, 67, 78, 89, 123, 234]

def test_case_4():
    sol = Solution()
    assert sol.sequentialDigits(1, 300) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 34, 45, 56, 67, 78, 89, 123, 234]

def test_case_5():
    sol = Solution()
    assert sol.sequentialDigits(99, 300) == [123, 234]

def test_case_6():
    sol = Solution()
    assert sol.sequentialDigits(100, 300) == [123, 234]

def test_case_7():
    sol = Solution()
    assert sol.sequentialDigits(101, 300) == [123, 234]

def test_case_8():
    sol = Solution()
    assert sol.sequentialDigits(200, 300) == [234]

def test_case_9():
    sol = Solution()
    assert sol.sequentialDigits(110, 300) == [123, 234]

def test_case_10():
    sol = Solution()
    assert sol.sequentialDigits(-1, 300) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 34, 45, 56, 67, 78, 89, 123, 234]

def test_case_11():
    sol = Solution()
    assert sol.sequentialDigits(100, 0) == []

def test_case_12():
    sol = Solution()
    assert sol.sequentialDigits(100, 1) == []

def test_case_13():
    sol = Solution()
    assert sol.sequentialDigits(100, 299) == [123, 234]

def test_case_14():
    sol = Solution()
    assert sol.sequentialDigits(100, 300) == [123, 234]

def test_case_15():
    sol = Solution()
    assert sol.sequentialDigits(100, 301) == [123, 234]

