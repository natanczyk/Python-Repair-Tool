# Test suite for wrong_medium_206  (slug: restore-the-array-from-adjacent-pairs)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_206.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.restoreArray([[2, 1], [3, 4], [3, 2]]) == [1, 2, 3, 4]

def test_case_2():
    sol = Solution()
    assert sol.restoreArray([[4, -2], [1, 4], [-3, 1]]) == [-2, 4, 1, -3]

def test_case_3():
    sol = Solution()
    assert sol.restoreArray([[100000, -100000]]) == [100000, -100000]

def test_case_4():
    sol = Solution()
    assert sol.restoreArray([[1, 2], [4, 3], [2, 3]]) == [1, 2, 3, 4]

def test_case_5():
    sol = Solution()
    assert sol.restoreArray([[3, 2], [3, 4], [2, 1]]) == [4, 3, 2, 1]

def test_case_6():
    sol = Solution()
    assert sol.restoreArray([[-2, 4], [4, 1], [1, -3]]) == [-2, 4, 1, -3]

def test_case_7():
    sol = Solution()
    assert sol.restoreArray([[-3, 1], [1, 4], [4, -2]]) == [-3, 1, 4, -2]

def test_case_8():
    sol = Solution()
    assert sol.restoreArray([[-100000, 100000]]) == [-100000, 100000]

def test_case_9():
    sol = Solution()
    assert sol.restoreArray([[100000, -100000]]) == [100000, -100000]

