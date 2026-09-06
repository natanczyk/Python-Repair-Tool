# Test suite for wrong_hard_013  (slug: minimum-time-to-complete-all-tasks)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_013.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.findMinimumTime([[2, 3, 1], [4, 5, 1], [1, 5, 2]]) == 2

def test_case_2():
    sol = Solution()
    assert sol.findMinimumTime([[1, 3, 2], [2, 5, 3], [5, 6, 2]]) == 4

def test_case_3():
    sol = Solution()
    assert sol.findMinimumTime([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0

def test_case_4():
    sol = Solution()
    assert sol.findMinimumTime([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 1

def test_case_5():
    sol = Solution()
    assert sol.findMinimumTime([[1, 3, 2], [1, 5, 4], [2, 5, 1]]) == 4

def test_case_6():
    sol = Solution()
    assert sol.findMinimumTime([[2, 3, 1], [1, 5, 2], [4, 5, 1]]) == 2

def test_case_7():
    sol = Solution()
    assert sol.findMinimumTime([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0

def test_case_8():
    sol = Solution()
    assert sol.findMinimumTime([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 1

def test_case_9():
    sol = Solution()
    assert sol.findMinimumTime([[2, 3, 1], [3, 5, 2], [2, 6, 5]]) == 5

def test_case_10():
    sol = Solution()
    assert sol.findMinimumTime([[1, 3, 2], [2, 5, 3], [5, 6, 2]]) == 4

