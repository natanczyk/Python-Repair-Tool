# Test suite for wrong_medium_133  (slug: make-costs-of-paths-equal-in-a-binary-tree)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_133.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.minIncrements(7, [34, 14, 11, 2, 3, 3, 1]) == 6

def test_case_2():
    sol = Solution()
    assert sol.minIncrements(3, [8, 3, 3]) == 0

def test_case_3():
    sol = Solution()
    assert sol.minIncrements(0, [34, 14, 11, 2, 3, 3, 1]) == 0

def test_case_4():
    sol = Solution()
    assert sol.minIncrements(1, [34, 14, 11, 2, 3, 3, 1]) == 0

def test_case_5():
    sol = Solution()
    assert sol.minIncrements(6, [34, 14, 11, 2, 3, 3, 1]) == 6

def test_case_6():
    sol = Solution()
    assert sol.minIncrements(7, [34, 14, 11, 2, 3, 3, 1]) == 6

def test_case_7():
    sol = Solution()
    assert sol.minIncrements(-1, [34, 14, 11, 2, 3, 3, 1]) == 0

def test_case_8():
    sol = Solution()
    assert sol.minIncrements(7, [8, 4, 7, 2, 3, 3, 5]) == 6

def test_case_9():
    sol = Solution()
    assert sol.minIncrements(7, [10, 5, 4, 2, 2, 1, 1]) == 1

def test_case_10():
    sol = Solution()
    assert sol.minIncrements(7, [9, 5, 8, 2, 2, 5, 1]) == 7

def test_case_11():
    sol = Solution()
    assert sol.minIncrements(7, [9, 8, 5, 2, 3, 3, 1, 0]) == 6

def test_case_12():
    sol = Solution()
    assert sol.minIncrements(7, [0, 0, 0, 0, 0, 0, 0]) == 0

def test_case_13():
    sol = Solution()
    assert sol.minIncrements(7, [3, 2, 2, 1, 1, 1, 1]) == 0

def test_case_14():
    sol = Solution()
    assert sol.minIncrements(7, [12, 10, 7, 3, 4, 4, 2]) == 6

def test_case_15():
    sol = Solution()
    assert sol.minIncrements(7, [6, 6, 3, 1, 2, 2, 0]) == 6

