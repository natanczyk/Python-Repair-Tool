# Test suite for wrong_medium_226  (slug: moving-stones-until-consecutive-ii)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_226.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.numMovesStonesII([4, 7, 9]) == [1, 2]

def test_case_2():
    sol = Solution()
    assert sol.numMovesStonesII([3, 4, 5, 6, 10]) == [2, 3]

def test_case_3():
    sol = Solution()
    assert sol.numMovesStonesII([4, 7, 9]) == [1, 2]

def test_case_4():
    sol = Solution()
    assert sol.numMovesStonesII([4, 7, 9]) == [1, 2]

def test_case_5():
    sol = Solution()
    assert sol.numMovesStonesII([4, 7, 9]) == [1, 2]

def test_case_6():
    sol = Solution()
    assert sol.numMovesStonesII([0, 4, 7, 9]) == [2, 5]

def test_case_7():
    sol = Solution()
    assert sol.numMovesStonesII([0, 0, 0]) == [4, -1]

def test_case_8():
    sol = Solution()
    assert sol.numMovesStonesII([1, 1, 1]) == [4, -1]

def test_case_9():
    sol = Solution()
    assert sol.numMovesStonesII([5, 8, 10]) == [1, 2]

def test_case_10():
    sol = Solution()
    assert sol.numMovesStonesII([3, 6, 8]) == [1, 2]

def test_case_11():
    sol = Solution()
    assert sol.numMovesStonesII([4, 4, 7, 7, 9, 9]) == [5, 1]

def test_case_12():
    sol = Solution()
    assert sol.numMovesStonesII([3, 4, 5, 6, 10]) == [2, 3]

def test_case_13():
    sol = Solution()
    assert sol.numMovesStonesII([3, 4, 5, 6, 10]) == [2, 3]

def test_case_14():
    sol = Solution()
    assert sol.numMovesStonesII([3, 4, 5, 6, 10]) == [2, 3]

def test_case_15():
    sol = Solution()
    assert sol.numMovesStonesII([0, 3, 4, 5, 6, 10]) == [3, 3]

