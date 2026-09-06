# Test suite for wrong_medium_023  (slug: sum-of-subarray-minimums)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_023.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.sumSubarrayMins([3, 1, 2, 4]) == 17

def test_case_2():
    sol = Solution()
    assert sol.sumSubarrayMins([11, 81, 94, 43, 3]) == 444

def test_case_3():
    sol = Solution()
    assert sol.sumSubarrayMins([]) == 0

def test_case_4():
    sol = Solution()
    assert sol.sumSubarrayMins([3]) == 3

def test_case_5():
    sol = Solution()
    assert sol.sumSubarrayMins([1, 2, 3, 4]) == 20

def test_case_6():
    sol = Solution()
    assert sol.sumSubarrayMins([4, 3, 2, 1]) == 20

def test_case_7():
    sol = Solution()
    assert sol.sumSubarrayMins([4, 2, 1, 3]) == 17

def test_case_8():
    sol = Solution()
    assert sol.sumSubarrayMins([3, 1, 2, 4, 0]) == 17

def test_case_9():
    sol = Solution()
    assert sol.sumSubarrayMins([0, 0, 0, 0]) == 0

def test_case_10():
    sol = Solution()
    assert sol.sumSubarrayMins([1, 1, 1, 1]) == 10

def test_case_11():
    sol = Solution()
    assert sol.sumSubarrayMins([4, 2, 3, 5]) == 27

def test_case_12():
    sol = Solution()
    assert sol.sumSubarrayMins([2, 0, 1, 3]) == 7

def test_case_13():
    sol = Solution()
    assert sol.sumSubarrayMins([3, 1, 2, 4, 3, 1, 2, 4]) == 53

def test_case_14():
    sol = Solution()
    assert sol.sumSubarrayMins([]) == 0

def test_case_15():
    sol = Solution()
    assert sol.sumSubarrayMins([11]) == 11

