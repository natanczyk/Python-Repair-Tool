# Test suite for wrong_easy_023  (slug: convert-integer-to-the-sum-of-two-no-zero-integers)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_023.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.getNoZeroIntegers(2) == [1, 1]

def test_case_2():
    sol = Solution()
    assert sol.getNoZeroIntegers(11) == [9, 2]

def test_case_3():
    sol = Solution()
    assert sol.getNoZeroIntegers(2) == [1, 1]

def test_case_4():
    sol = Solution()
    assert sol.getNoZeroIntegers(3) == [2, 1]

def test_case_5():
    sol = Solution()
    assert sol.getNoZeroIntegers(4) == [3, 1]

def test_case_6():
    sol = Solution()
    assert sol.getNoZeroIntegers(12) == [11, 1]

def test_case_7():
    sol = Solution()
    assert sol.getNoZeroIntegers(10) == [9, 1]

def test_case_8():
    sol = Solution()
    assert sol.getNoZeroIntegers(11) == [9, 2]

def test_case_9():
    sol = Solution()
    assert sol.getNoZeroIntegers(12) == [11, 1]

def test_case_10():
    sol = Solution()
    assert sol.getNoZeroIntegers(21) == [19, 2]

def test_case_11():
    sol = Solution()
    assert sol.getNoZeroIntegers(22) == [21, 1]

