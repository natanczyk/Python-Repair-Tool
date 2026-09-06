# Test suite for wrong_medium_126  (slug: maximum-number-of-moves-in-a-grid)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_126.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]) == 3

def test_case_2():
    sol = Solution()
    assert sol.maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]) == 0

def test_case_3():
    sol = Solution()
    assert sol.maxMoves([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) == 0

def test_case_4():
    sol = Solution()
    assert sol.maxMoves([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 0

def test_case_5():
    sol = Solution()
    assert sol.maxMoves([[5, 3, 4, 2], [3, 9, 4, 5], [11, 2, 4, 3], [15, 13, 9, 10]]) == 1

def test_case_6():
    sol = Solution()
    assert sol.maxMoves([[10, 9, 13, 15], [3, 4, 2, 11], [5, 4, 9, 3], [2, 4, 3, 5]]) == 3

def test_case_7():
    sol = Solution()
    assert sol.maxMoves([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0

def test_case_8():
    sol = Solution()
    assert sol.maxMoves([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 0

def test_case_9():
    sol = Solution()
    assert sol.maxMoves([[4, 2, 3], [9, 1, 2], [7, 1, 1]]) == 0

def test_case_10():
    sol = Solution()
    assert sol.maxMoves([[1, 1, 7], [2, 1, 9], [3, 2, 4]]) == 0

