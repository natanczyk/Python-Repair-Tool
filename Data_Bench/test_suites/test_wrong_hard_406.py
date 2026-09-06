# Test suite for wrong_hard_406  (slug: max-points-on-a-line)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_406.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3

def test_case_2():
    sol = Solution()
    assert sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4

def test_case_3():
    sol = Solution()
    assert sol.maxPoints([[0, 0], [0, 0], [0, 0]]) == 1

def test_case_4():
    sol = Solution()
    assert sol.maxPoints([[1, 1], [1, 1], [1, 1]]) == 1

def test_case_5():
    sol = Solution()
    assert sol.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3

def test_case_6():
    sol = Solution()
    assert sol.maxPoints([[3, 3], [2, 2], [1, 1]]) == 3

def test_case_7():
    sol = Solution()
    assert sol.maxPoints([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]) == 1

def test_case_8():
    sol = Solution()
    assert sol.maxPoints([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]) == 1

def test_case_9():
    sol = Solution()
    assert sol.maxPoints([[1, 1], [2, 3], [3, 5], [1, 4], [3, 2], [4, 1]]) == 4

def test_case_10():
    sol = Solution()
    assert sol.maxPoints([[1, 4], [2, 3], [4, 1], [5, 3], [3, 2], [1, 1]]) == 4

