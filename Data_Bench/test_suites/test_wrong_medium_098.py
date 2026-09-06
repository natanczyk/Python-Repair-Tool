# Test suite for wrong_medium_098  (slug: grid-game)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_098.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.gridGame([[2, 5, 4], [1, 5, 1]]) == 4

def test_case_2():
    sol = Solution()
    assert sol.gridGame([[3, 3, 1], [8, 5, 2]]) == 4

def test_case_3():
    sol = Solution()
    assert sol.gridGame([[1, 3, 1, 15], [1, 3, 3, 1]]) == 7

def test_case_4():
    sol = Solution()
    assert sol.gridGame([[0, 0, 0], [0, 0, 0]]) == 0

def test_case_5():
    sol = Solution()
    assert sol.gridGame([[1, 1, 1], [1, 1, 1]]) == 1

def test_case_6():
    sol = Solution()
    assert sol.gridGame([[4, 5, 2], [1, 5, 1]]) == 2

def test_case_7():
    sol = Solution()
    assert sol.gridGame([[1, 5, 1], [2, 5, 4]]) == 2

def test_case_8():
    sol = Solution()
    assert sol.gridGame([[0, 0, 0], [0, 0, 0]]) == 0

def test_case_9():
    sol = Solution()
    assert sol.gridGame([[1, 1, 1], [1, 1, 1]]) == 1

def test_case_10():
    sol = Solution()
    assert sol.gridGame([[1, 3, 3], [2, 5, 8]]) == 3

def test_case_11():
    sol = Solution()
    assert sol.gridGame([[8, 5, 2], [3, 3, 1]]) == 3

def test_case_12():
    sol = Solution()
    assert sol.gridGame([[0, 0, 0, 0], [0, 0, 0, 0]]) == 0

def test_case_13():
    sol = Solution()
    assert sol.gridGame([[1, 1, 1, 1], [1, 1, 1, 1]]) == 2

def test_case_14():
    sol = Solution()
    assert sol.gridGame([[15, 1, 3, 1], [1, 3, 3, 1]]) == 4

def test_case_15():
    sol = Solution()
    assert sol.gridGame([[1, 3, 3, 1], [1, 3, 1, 15]]) == 4

