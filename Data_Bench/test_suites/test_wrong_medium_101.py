# Test suite for wrong_medium_101  (slug: number-of-ways-to-split-array)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_101.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.waysToSplitArray([10, 4, -8, 7]) == 2

def test_case_2():
    sol = Solution()
    assert sol.waysToSplitArray([2, 3, 1, 0]) == 2

def test_case_3():
    sol = Solution()
    assert sol.waysToSplitArray([10]) == 1

def test_case_4():
    sol = Solution()
    assert sol.waysToSplitArray([-8, 4, 7, 10]) == 0

def test_case_5():
    sol = Solution()
    assert sol.waysToSplitArray([10, 7, 4, -8]) == 3

def test_case_6():
    sol = Solution()
    assert sol.waysToSplitArray([7, -8, 4, 10]) == 1

def test_case_7():
    sol = Solution()
    assert sol.waysToSplitArray([10, 4, -8, 7, 0]) == 3

def test_case_8():
    sol = Solution()
    assert sol.waysToSplitArray([0, 0, 0, 0]) == 3

def test_case_9():
    sol = Solution()
    assert sol.waysToSplitArray([1, 1, 1, 1]) == 2

def test_case_10():
    sol = Solution()
    assert sol.waysToSplitArray([11, 5, -7, 8]) == 3

def test_case_11():
    sol = Solution()
    assert sol.waysToSplitArray([9, 3, -9, 6]) == 2

def test_case_12():
    sol = Solution()
    assert sol.waysToSplitArray([10, 4, -8, 7, 10, 4, -8, 7]) == 5

def test_case_13():
    sol = Solution()
    assert sol.waysToSplitArray([-8, 10, 4, 7]) == 0

def test_case_14():
    sol = Solution()
    assert sol.waysToSplitArray([2]) == 1

def test_case_15():
    sol = Solution()
    assert sol.waysToSplitArray([0, 1, 2, 3]) == 1

