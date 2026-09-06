# Test suite for wrong_hard_203  (slug: n-queens-ii)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_203.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.totalNQueens(4) == 2

def test_case_2():
    sol = Solution()
    assert sol.totalNQueens(1) == 1

def test_case_3():
    sol = Solution()
    assert sol.totalNQueens(0) == 1

def test_case_4():
    sol = Solution()
    assert sol.totalNQueens(1) == 1

def test_case_5():
    sol = Solution()
    assert sol.totalNQueens(3) == 0

def test_case_6():
    sol = Solution()
    assert sol.totalNQueens(4) == 2

def test_case_7():
    sol = Solution()
    assert sol.totalNQueens(5) == 10

def test_case_8():
    sol = Solution()
    assert sol.totalNQueens(8) == 92

