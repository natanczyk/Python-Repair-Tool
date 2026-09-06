# Test suite for wrong_easy_042  (slug: make-array-zero-by-subtracting-equal-amounts)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_042.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.minimumOperations([1, 5, 0, 3, 5]) == 3

def test_case_2():
    sol = Solution()
    assert sol.minimumOperations([0]) == 0

def test_case_3():
    sol = Solution()
    assert sol.minimumOperations([]) == 0

def test_case_4():
    sol = Solution()
    assert sol.minimumOperations([1]) == 1

def test_case_5():
    sol = Solution()
    assert sol.minimumOperations([0, 1, 3, 5, 5]) == 3

def test_case_6():
    sol = Solution()
    assert sol.minimumOperations([5, 5, 3, 1, 0]) == 3

def test_case_7():
    sol = Solution()
    assert sol.minimumOperations([5, 3, 0, 5, 1]) == 3

def test_case_8():
    sol = Solution()
    assert sol.minimumOperations([1, 5, 0, 3, 5, 0]) == 3

def test_case_9():
    sol = Solution()
    assert sol.minimumOperations([0, 0, 0, 0, 0]) == 0

def test_case_10():
    sol = Solution()
    assert sol.minimumOperations([1, 1, 1, 1, 1]) == 1

def test_case_11():
    sol = Solution()
    assert sol.minimumOperations([2, 6, 1, 4, 6]) == 4

def test_case_12():
    sol = Solution()
    assert sol.minimumOperations([0, 4, -1, 2, 4]) == 3

def test_case_13():
    sol = Solution()
    assert sol.minimumOperations([1, 5, 0, 3, 5, 1, 5, 0, 3, 5]) == 3

def test_case_14():
    sol = Solution()
    assert sol.minimumOperations([0, 1, 3, 5]) == 3

def test_case_15():
    sol = Solution()
    assert sol.minimumOperations([]) == 0

