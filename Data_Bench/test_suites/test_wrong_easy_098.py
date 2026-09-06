# Test suite for wrong_easy_098  (slug: count-equal-and-divisible-pairs-in-an-array)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_098.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.countPairs([3, 1, 2, 2, 2, 1, 3], 2) == 4

def test_case_2():
    sol = Solution()
    assert sol.countPairs([1, 2, 3, 4], 1) == 0

def test_case_3():
    sol = Solution()
    assert sol.countPairs([], 2) == 0

def test_case_4():
    sol = Solution()
    assert sol.countPairs([3], 2) == 0

def test_case_5():
    sol = Solution()
    assert sol.countPairs([1, 1, 2, 2, 2, 3, 3], 2) == 5

def test_case_6():
    sol = Solution()
    assert sol.countPairs([3, 3, 2, 2, 2, 1, 1], 2) == 5

def test_case_7():
    sol = Solution()
    assert sol.countPairs([3, 1, 2, 2, 2, 1, 3], 2) == 4

def test_case_8():
    sol = Solution()
    assert sol.countPairs([3, 1, 2, 2, 2, 1, 3, 0], 2) == 4

def test_case_9():
    sol = Solution()
    assert sol.countPairs([0, 0, 0, 0, 0, 0, 0], 2) == 18

def test_case_10():
    sol = Solution()
    assert sol.countPairs([1, 1, 1, 1, 1, 1, 1], 2) == 18

def test_case_11():
    sol = Solution()
    assert sol.countPairs([4, 2, 3, 3, 3, 2, 4], 2) == 4

def test_case_12():
    sol = Solution()
    assert sol.countPairs([2, 0, 1, 1, 1, 0, 2], 2) == 4

def test_case_13():
    sol = Solution()
    assert sol.countPairs([3, 1, 2, 2, 2, 1, 3, 3, 1, 2, 2, 2, 1, 3], 2) == 22

def test_case_14():
    sol = Solution()
    assert sol.countPairs([1, 2, 3], 2) == 0

def test_case_15():
    sol = Solution()
    assert sol.countPairs([3, 1, 2, 2, 2, 1, 3], 1) == 5

