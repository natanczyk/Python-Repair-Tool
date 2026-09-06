# Test suite for wrong_hard_040  (slug: next-greater-element-iv)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_040.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.secondGreaterElement([2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1]

def test_case_2():
    sol = Solution()
    assert sol.secondGreaterElement([3, 3]) == [-1, -1]

def test_case_3():
    sol = Solution()
    assert sol.secondGreaterElement([]) == []

def test_case_4():
    sol = Solution()
    assert sol.secondGreaterElement([2]) == [-1]

def test_case_5():
    sol = Solution()
    assert sol.secondGreaterElement([0, 2, 4, 6, 9]) == [4, 6, 9, -1, -1]

def test_case_6():
    sol = Solution()
    assert sol.secondGreaterElement([9, 6, 4, 2, 0]) == [-1, -1, -1, -1, -1]

def test_case_7():
    sol = Solution()
    assert sol.secondGreaterElement([6, 9, 0, 4, 2]) == [-1, -1, 2, -1, -1]

def test_case_8():
    sol = Solution()
    assert sol.secondGreaterElement([2, 4, 0, 9, 6, 0]) == [9, 6, 6, -1, -1, -1]

def test_case_9():
    sol = Solution()
    assert sol.secondGreaterElement([0, 0, 0, 0, 0]) == [-1, -1, -1, -1, -1]

def test_case_10():
    sol = Solution()
    assert sol.secondGreaterElement([1, 1, 1, 1, 1]) == [-1, -1, -1, -1, -1]

def test_case_11():
    sol = Solution()
    assert sol.secondGreaterElement([3, 5, 1, 10, 7]) == [10, 7, 7, -1, -1]

def test_case_12():
    sol = Solution()
    assert sol.secondGreaterElement([1, 3, -1, 8, 5]) == [8, 5, 5, -1, -1]

def test_case_13():
    sol = Solution()
    assert sol.secondGreaterElement([2, 4, 0, 9, 6, 2, 4, 0, 9, 6]) == [9, 6, 6, -1, -1, 9, 6, 6, -1, -1]

def test_case_14():
    sol = Solution()
    assert sol.secondGreaterElement([]) == []

def test_case_15():
    sol = Solution()
    assert sol.secondGreaterElement([3]) == [-1]

