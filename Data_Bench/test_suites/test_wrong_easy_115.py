# Test suite for wrong_easy_115  (slug: average-value-of-even-numbers-that-are-divisible-by-three)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_115.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.averageValue([1, 3, 6, 10, 12, 15]) == 9

def test_case_2():
    sol = Solution()
    assert sol.averageValue([1, 2, 4, 7, 10]) == 0

def test_case_3():
    sol = Solution()
    assert sol.averageValue([]) == 0

def test_case_4():
    sol = Solution()
    assert sol.averageValue([1]) == 0

def test_case_5():
    sol = Solution()
    assert sol.averageValue([1, 3, 6, 10, 12, 15]) == 9

def test_case_6():
    sol = Solution()
    assert sol.averageValue([15, 12, 10, 6, 3, 1]) == 9

def test_case_7():
    sol = Solution()
    assert sol.averageValue([1, 3, 6, 10, 12, 15, 0]) == 6

def test_case_8():
    sol = Solution()
    assert sol.averageValue([0, 0, 0, 0, 0, 0]) == 0

def test_case_9():
    sol = Solution()
    assert sol.averageValue([1, 1, 1, 1, 1, 1]) == 0

def test_case_10():
    sol = Solution()
    assert sol.averageValue([2, 4, 7, 11, 13, 16]) == 0

def test_case_11():
    sol = Solution()
    assert sol.averageValue([0, 2, 5, 9, 11, 14]) == 0

def test_case_12():
    sol = Solution()
    assert sol.averageValue([1, 3, 6, 10, 12, 15, 1, 3, 6, 10, 12, 15]) == 9

def test_case_13():
    sol = Solution()
    assert sol.averageValue([]) == 0

def test_case_14():
    sol = Solution()
    assert sol.averageValue([1]) == 0

def test_case_15():
    sol = Solution()
    assert sol.averageValue([1, 2, 4, 7, 10]) == 0

