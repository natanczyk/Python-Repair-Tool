# Test suite for wrong_medium_146  (slug: partition-array-according-to-given-pivot)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_146.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.pivotArray([9, 12, 5, 10, 14, 3, 10], 10) == [9, 5, 3, 10, 10, 12, 14]

def test_case_2():
    sol = Solution()
    assert sol.pivotArray([-3, 4, 3, 2], 2) == [-3, 2, 4, 3]

def test_case_3():
    sol = Solution()
    assert sol.pivotArray([], 10) == []

def test_case_4():
    sol = Solution()
    assert sol.pivotArray([9], 10) == [9]

def test_case_5():
    sol = Solution()
    assert sol.pivotArray([3, 5, 9, 10, 10, 12, 14], 10) == [3, 5, 9, 10, 10, 12, 14]

def test_case_6():
    sol = Solution()
    assert sol.pivotArray([14, 12, 10, 10, 9, 5, 3], 10) == [9, 5, 3, 10, 10, 14, 12]

def test_case_7():
    sol = Solution()
    assert sol.pivotArray([10, 3, 14, 10, 5, 12, 9], 10) == [3, 5, 9, 10, 10, 14, 12]

def test_case_8():
    sol = Solution()
    assert sol.pivotArray([9, 12, 5, 10, 14, 3, 10, 0], 10) == [9, 5, 3, 0, 10, 10, 12, 14]

def test_case_9():
    sol = Solution()
    assert sol.pivotArray([0, 0, 0, 0, 0, 0, 0], 10) == [0, 0, 0, 0, 0, 0, 0]

def test_case_10():
    sol = Solution()
    assert sol.pivotArray([1, 1, 1, 1, 1, 1, 1], 10) == [1, 1, 1, 1, 1, 1, 1]

def test_case_11():
    sol = Solution()
    assert sol.pivotArray([10, 13, 6, 11, 15, 4, 11], 10) == [6, 4, 10, 13, 11, 15, 11]

def test_case_12():
    sol = Solution()
    assert sol.pivotArray([8, 11, 4, 9, 13, 2, 9], 10) == [8, 4, 9, 2, 9, 11, 13]

def test_case_13():
    sol = Solution()
    assert sol.pivotArray([9, 12, 5, 10, 14, 3, 10, 9, 12, 5, 10, 14, 3, 10], 10) == [9, 5, 3, 9, 5, 3, 10, 10, 10, 10, 12, 14, 12, 14]

def test_case_14():
    sol = Solution()
    assert sol.pivotArray([3, 5, 9, 10, 12, 14], 10) == [3, 5, 9, 10, 12, 14]

def test_case_15():
    sol = Solution()
    assert sol.pivotArray([9, 12, 5, 10, 14, 3, 10], 0) == [9, 12, 5, 10, 14, 3, 10]

