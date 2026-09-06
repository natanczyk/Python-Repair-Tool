# Test suite for wrong_easy_320  (slug: how-many-numbers-are-smaller-than-the-current-number)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_320.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]

def test_case_2():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3]

def test_case_3():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0]

def test_case_4():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([]) == []

def test_case_5():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([8]) == [0]

def test_case_6():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([1, 2, 2, 3, 8]) == [0, 1, 1, 3, 4]

def test_case_7():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([8, 3, 2, 2, 1]) == [4, 3, 1, 1, 0]

def test_case_8():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([3, 2, 2, 1, 8]) == [3, 1, 1, 0, 4]

def test_case_9():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3, 0]) == [5, 1, 2, 2, 4, 0]

def test_case_10():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

def test_case_11():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0]

def test_case_12():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([9, 2, 3, 3, 4]) == [4, 0, 1, 1, 3]

def test_case_13():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([7, 0, 1, 1, 2]) == [4, 0, 1, 1, 3]

def test_case_14():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3, 8, 1, 2, 2, 3]) == [8, 0, 2, 2, 6, 8, 0, 2, 2, 6]

def test_case_15():
    sol = Solution()
    assert sol.smallerNumbersThanCurrent([8, 1, 2, 3]) == [3, 0, 1, 2]

