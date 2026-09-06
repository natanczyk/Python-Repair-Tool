# Test suite for wrong_easy_339  (slug: binary-search)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_339.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4

def test_case_2():
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1

def test_case_3():
    sol = Solution()
    assert sol.search([], 9) == -1

def test_case_4():
    sol = Solution()
    assert sol.search([-1], 9) == -1

def test_case_5():
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4

def test_case_6():
    sol = Solution()
    assert sol.search([12, 9, 5, 3, 0, -1], 9) == 6

def test_case_7():
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12, 0], 9) == 4

def test_case_8():
    sol = Solution()
    assert sol.search([0, 0, 0, 0, 0, 0], 9) == -1

def test_case_9():
    sol = Solution()
    assert sol.search([1, 1, 1, 1, 1, 1], 9) == -1

def test_case_10():
    sol = Solution()
    assert sol.search([0, 1, 4, 6, 10, 13], 9) == -1

def test_case_11():
    sol = Solution()
    assert sol.search([-2, -1, 2, 4, 8, 11], 9) == -1

def test_case_12():
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12, -1, 0, 3, 5, 9, 12], 9) == 10

def test_case_13():
    sol = Solution()
    assert sol.search([0, 3, 5, 9, 12, -1], 9) == 3

def test_case_14():
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 0) == 1

def test_case_15():
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 1) == -1

