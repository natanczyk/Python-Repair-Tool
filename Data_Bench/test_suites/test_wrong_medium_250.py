# Test suite for wrong_medium_250  (slug: maximum-strength-of-a-group)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_250.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.maxStrength([3, -1, -5, 2, 5, -9]) == 1350

def test_case_2():
    sol = Solution()
    assert sol.maxStrength([-4, -5, -4]) == 20

def test_case_3():
    sol = Solution()
    assert sol.maxStrength([3]) == 3

def test_case_4():
    sol = Solution()
    assert sol.maxStrength([-9, -5, -1, 2, 3, 5]) == 1350

def test_case_5():
    sol = Solution()
    assert sol.maxStrength([5, 3, 2, -1, -5, -9]) == 1350

def test_case_6():
    sol = Solution()
    assert sol.maxStrength([-9, 5, 2, -5, -1, 3]) == 1350

def test_case_7():
    sol = Solution()
    assert sol.maxStrength([3, -1, -5, 2, 5, -9, 0]) == 1350

def test_case_8():
    sol = Solution()
    assert sol.maxStrength([0, 0, 0, 0, 0, 0]) == 0

def test_case_9():
    sol = Solution()
    assert sol.maxStrength([1, 1, 1, 1, 1, 1]) == 1

def test_case_10():
    sol = Solution()
    assert sol.maxStrength([4, 0, -4, 3, 6, -8]) == 2304

def test_case_11():
    sol = Solution()
    assert sol.maxStrength([2, -2, -6, 1, 4, -10]) == 480

def test_case_12():
    sol = Solution()
    assert sol.maxStrength([3, -1, -5, 2, 5, -9, 3, -1, -5, 2, 5, -9]) == 1822500

def test_case_13():
    sol = Solution()
    assert sol.maxStrength([2, 3, 5, -9, -5, -1]) == 1350

def test_case_14():
    sol = Solution()
    assert sol.maxStrength([-4]) == -4

def test_case_15():
    sol = Solution()
    assert sol.maxStrength([-5, -4, -4]) == 20

