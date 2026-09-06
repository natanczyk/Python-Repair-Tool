# Test suite for wrong_medium_511  (slug: find-players-with-zero-or-one-losses)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_511.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]) == [[1, 2, 10], [4, 5, 7, 8]]

def test_case_2():
    sol = Solution()
    assert sol.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]) == [[1, 2, 5, 6], []]

def test_case_3():
    sol = Solution()
    assert sol.findWinners([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]) == [[], []]

def test_case_4():
    sol = Solution()
    assert sol.findWinners([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == [[], []]

def test_case_5():
    sol = Solution()
    assert sol.findWinners([[3, 1], [3, 2], [6, 3], [6, 5], [7, 5], [5, 4], [8, 4], [9, 4], [4, 10], [9, 10]]) == [[6, 7, 8, 9], [1, 2, 3]]

def test_case_6():
    sol = Solution()
    assert sol.findWinners([[10, 9], [10, 4], [4, 9], [4, 8], [4, 5], [5, 7], [5, 6], [3, 6], [2, 3], [1, 3]]) == [[1, 2, 10], [4, 5, 7, 8]]

def test_case_7():
    sol = Solution()
    assert sol.findWinners([[0, 0], [0, 0], [0, 0], [0, 0]]) == [[], []]

def test_case_8():
    sol = Solution()
    assert sol.findWinners([[1, 1], [1, 1], [1, 1], [1, 1]]) == [[], []]

def test_case_9():
    sol = Solution()
    assert sol.findWinners([[3, 2], [3, 1], [4, 5], [4, 6]]) == [[3, 4], [1, 2, 5, 6]]

def test_case_10():
    sol = Solution()
    assert sol.findWinners([[6, 4], [5, 4], [1, 3], [2, 3]]) == [[1, 2, 5, 6], []]

