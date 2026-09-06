# Test suite for wrong_medium_403  (slug: sum-of-absolute-differences-in-a-sorted-array)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_403.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([2, 3, 5]) == [4, 3, 5]

def test_case_2():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([1, 4, 6, 8, 10]) == [24, 15, 13, 15, 21]

def test_case_3():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([]) == []

def test_case_4():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([2]) == [0]

def test_case_5():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([2, 3, 5]) == [4, 3, 5]

def test_case_6():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([5, 3, 2]) == [5, 3, 4]

def test_case_7():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([2, 3, 5, 0]) == [2, 2, 10, 10]

def test_case_8():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([0, 0, 0]) == [0, 0, 0]

def test_case_9():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([1, 1, 1]) == [0, 0, 0]

def test_case_10():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([3, 4, 6]) == [4, 3, 5]

def test_case_11():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([1, 2, 4]) == [4, 3, 5]

def test_case_12():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([2, 3, 5, 2, 3, 5]) == [8, 4, 10, 8, 2, 10]

def test_case_13():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([]) == []

def test_case_14():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([1]) == [0]

def test_case_15():
    sol = Solution()
    assert sol.getSumAbsoluteDifferences([1, 4, 6, 8, 10]) == [24, 15, 13, 15, 21]

