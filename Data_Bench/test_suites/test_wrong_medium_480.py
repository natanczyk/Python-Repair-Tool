# Test suite for wrong_medium_480  (slug: maximum-of-absolute-value-expression)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_480.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.maxAbsValExpr([1, 2, 3, 4], [-1, 4, 5, 6]) == 13

def test_case_2():
    sol = Solution()
    assert sol.maxAbsValExpr([1, -2, -5, 0, 10], [0, -2, -1, -7, -4]) == 20

def test_case_3():
    sol = Solution()
    assert sol.maxAbsValExpr([1], [-1, 4, 5, 6]) == 0

def test_case_4():
    sol = Solution()
    assert sol.maxAbsValExpr([1, 2, 3, 4], [-1, 4, 5, 6]) == 13

def test_case_5():
    sol = Solution()
    assert sol.maxAbsValExpr([4, 3, 2, 1], [-1, 4, 5, 6]) == 13

def test_case_6():
    sol = Solution()
    assert sol.maxAbsValExpr([0, 0, 0, 0], [-1, 4, 5, 6]) == 10

def test_case_7():
    sol = Solution()
    assert sol.maxAbsValExpr([1, 1, 1, 1], [-1, 4, 5, 6]) == 10

def test_case_8():
    sol = Solution()
    assert sol.maxAbsValExpr([2, 3, 4, 5], [-1, 4, 5, 6]) == 13

def test_case_9():
    sol = Solution()
    assert sol.maxAbsValExpr([0, 1, 2, 3], [-1, 4, 5, 6]) == 13

def test_case_10():
    sol = Solution()
    assert sol.maxAbsValExpr([1, 2, 3, 4], [-1, 4, 5, 6]) == 13

def test_case_11():
    sol = Solution()
    assert sol.maxAbsValExpr([1, 2, 3, 4], [6, 5, 4, -1]) == 13

def test_case_12():
    sol = Solution()
    assert sol.maxAbsValExpr([1, 2, 3, 4], [-1, 4, 5, 6, 0]) == 13

def test_case_13():
    sol = Solution()
    assert sol.maxAbsValExpr([1, 2, 3, 4], [0, 0, 0, 0]) == 6

def test_case_14():
    sol = Solution()
    assert sol.maxAbsValExpr([1, 2, 3, 4], [1, 1, 1, 1]) == 6

def test_case_15():
    sol = Solution()
    assert sol.maxAbsValExpr([1, 2, 3, 4], [0, 5, 6, 7]) == 13

