# Test suite for wrong_easy_039  (slug: kth-missing-positive-number)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_039.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.findKthPositive([2, 3, 4, 7, 11], 5) == 9

def test_case_2():
    sol = Solution()
    assert sol.findKthPositive([1, 2, 3, 4], 2) == 6

def test_case_3():
    sol = Solution()
    assert sol.findKthPositive([], 5) == 5

def test_case_4():
    sol = Solution()
    assert sol.findKthPositive([2], 5) == 6

def test_case_5():
    sol = Solution()
    assert sol.findKthPositive([2, 3, 4, 7, 11], 5) == 9

def test_case_6():
    sol = Solution()
    assert sol.findKthPositive([11, 7, 4, 3, 2], 5) == 10

def test_case_7():
    sol = Solution()
    assert sol.findKthPositive([2, 3, 4, 7, 11, 0], 5) == 11

def test_case_8():
    sol = Solution()
    assert sol.findKthPositive([0, 0, 0, 0, 0], 5) == 10

def test_case_9():
    sol = Solution()
    assert sol.findKthPositive([1, 1, 1, 1, 1], 5) == 10

def test_case_10():
    sol = Solution()
    assert sol.findKthPositive([3, 4, 5, 8, 12], 5) == 9

def test_case_11():
    sol = Solution()
    assert sol.findKthPositive([1, 2, 3, 6, 10], 5) == 9

def test_case_12():
    sol = Solution()
    assert sol.findKthPositive([2, 3, 4, 7, 11, 2, 3, 4, 7, 11], 5) == 15

def test_case_13():
    sol = Solution()
    assert sol.findKthPositive([2, 3, 4, 7, 11], 0) == 0

def test_case_14():
    sol = Solution()
    assert sol.findKthPositive([2, 3, 4, 7, 11], 1) == 1

def test_case_15():
    sol = Solution()
    assert sol.findKthPositive([2, 3, 4, 7, 11], 4) == 8

