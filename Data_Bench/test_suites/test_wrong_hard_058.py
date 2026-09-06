# Test suite for wrong_hard_058  (slug: create-components-with-same-value)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_058.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.componentValue([6, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 2

def test_case_2():
    sol = Solution()
    assert sol.componentValue([2], []) == 0

def test_case_3():
    sol = Solution()
    assert sol.componentValue([2, 2, 2, 6, 6], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 2

def test_case_4():
    sol = Solution()
    assert sol.componentValue([6, 6, 2, 2, 2], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 0

def test_case_5():
    sol = Solution()
    assert sol.componentValue([6, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 2

def test_case_6():
    sol = Solution()
    assert sol.componentValue([6, 2, 2, 2, 6, 0], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 2

def test_case_7():
    sol = Solution()
    assert sol.componentValue([0, 0, 0, 0, 0], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 0

def test_case_8():
    sol = Solution()
    assert sol.componentValue([1, 1, 1, 1, 1], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 4

def test_case_9():
    sol = Solution()
    assert sol.componentValue([7, 3, 3, 3, 7], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 0

def test_case_10():
    sol = Solution()
    assert sol.componentValue([5, 1, 1, 1, 5], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 0

def test_case_11():
    sol = Solution()
    assert sol.componentValue([6, 2, 2, 2, 6, 6, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 5

def test_case_12():
    sol = Solution()
    assert sol.componentValue([6, 2, 2, 2, 6], [[0, 0], [0, 0], [0, 0], [0, 0]]) == 2

def test_case_13():
    sol = Solution()
    assert sol.componentValue([6, 2, 2, 2, 6], [[1, 1], [1, 1], [1, 1], [1, 1]]) == 2

def test_case_14():
    sol = Solution()
    assert sol.componentValue([6, 2, 2, 2, 6], [[1, 0], [2, 1], [3, 1], [4, 3]]) == 2

def test_case_15():
    sol = Solution()
    assert sol.componentValue([6, 2, 2, 2, 6], [[3, 4], [1, 3], [1, 2], [0, 1]]) == 2

