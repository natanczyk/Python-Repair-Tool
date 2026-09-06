# Test suite for wrong_easy_292  (slug: plus-one)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_292.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]

def test_case_2():
    sol = Solution()
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]

def test_case_3():
    sol = Solution()
    assert sol.plusOne([9]) == [1, 0]

def test_case_4():
    sol = Solution()
    assert sol.plusOne([1]) == [2]

def test_case_5():
    sol = Solution()
    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]

def test_case_6():
    sol = Solution()
    assert sol.plusOne([3, 2, 1]) == [3, 2, 2]

def test_case_7():
    sol = Solution()
    assert sol.plusOne([1, 2, 3, 0]) == [1, 2, 3, 1]

def test_case_8():
    sol = Solution()
    assert sol.plusOne([0, 0, 0]) == [1]

def test_case_9():
    sol = Solution()
    assert sol.plusOne([1, 1, 1]) == [1, 1, 2]

def test_case_10():
    sol = Solution()
    assert sol.plusOne([2, 3, 4]) == [2, 3, 5]

def test_case_11():
    sol = Solution()
    assert sol.plusOne([0, 1, 2]) == [1, 3]

def test_case_12():
    sol = Solution()
    assert sol.plusOne([1, 2, 3, 1, 2, 3]) == [1, 2, 3, 1, 2, 4]

def test_case_13():
    sol = Solution()
    assert sol.plusOne([4]) == [5]

def test_case_14():
    sol = Solution()
    assert sol.plusOne([1, 2, 3, 4]) == [1, 2, 3, 5]

def test_case_15():
    sol = Solution()
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]

