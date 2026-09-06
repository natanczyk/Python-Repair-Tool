# Test suite for wrong_hard_046  (slug: frog-position-after-t-seconds)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_046.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4) == 0.16666666666666666

def test_case_2():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1, 7) == 0.3333333333333333

def test_case_3():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4) == 0.16666666666666666

def test_case_4():
    sol = Solution()
    assert sol.frogPosition(8, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4) == 0.16666666666666666

def test_case_5():
    sol = Solution()
    assert sol.frogPosition(14, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4) == 0.16666666666666666

def test_case_6():
    sol = Solution()
    assert sol.frogPosition(17, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4) == 0.16666666666666666

def test_case_7():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], 2, 4) == 0

def test_case_8():
    sol = Solution()
    assert sol.frogPosition(7, [[2, 1], [3, 1], [7, 1], [4, 2], [6, 2], [5, 3]], 2, 4) == 0.16666666666666666

def test_case_9():
    sol = Solution()
    assert sol.frogPosition(7, [[3, 5], [2, 6], [2, 4], [1, 7], [1, 3], [1, 2]], 2, 4) == 0.16666666666666666

def test_case_10():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 0, 4) == 0

def test_case_11():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1, 4) == 0

def test_case_12():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4) == 0.16666666666666666

def test_case_13():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 3, 4) == 0.16666666666666666

def test_case_14():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 4, 4) == 0.16666666666666666

def test_case_15():
    sol = Solution()
    assert sol.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 12, 4) == 0.16666666666666666

