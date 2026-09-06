# Test suite for wrong_medium_112  (slug: minimize-maximum-pair-sum-in-array)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_112.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.minPairSum([2, 3, 3, 5]) == 7

def test_case_2():
    sol = Solution()
    assert sol.minPairSum([2, 3, 4, 4, 5, 6]) == 8

def test_case_3():
    sol = Solution()
    assert sol.minPairSum([2, 3, 3, 5]) == 7

def test_case_4():
    sol = Solution()
    assert sol.minPairSum([2, 3, 3, 5]) == 7

def test_case_5():
    sol = Solution()
    assert sol.minPairSum([2, 3, 3, 5]) == 7

def test_case_6():
    sol = Solution()
    assert sol.minPairSum([0, 2, 3, 3, 5]) == 5

def test_case_7():
    sol = Solution()
    assert sol.minPairSum([0, 0, 0, 0]) == 0

def test_case_8():
    sol = Solution()
    assert sol.minPairSum([1, 1, 1, 1]) == 2

def test_case_9():
    sol = Solution()
    assert sol.minPairSum([3, 4, 4, 6]) == 9

def test_case_10():
    sol = Solution()
    assert sol.minPairSum([1, 2, 2, 4]) == 5

def test_case_11():
    sol = Solution()
    assert sol.minPairSum([2, 2, 3, 3, 3, 3, 5, 5]) == 7

def test_case_12():
    sol = Solution()
    assert sol.minPairSum([2, 3, 5]) == 7

def test_case_13():
    sol = Solution()
    assert sol.minPairSum([2, 3, 4, 4, 5, 6]) == 8

def test_case_14():
    sol = Solution()
    assert sol.minPairSum([2, 3, 4, 4, 5, 6]) == 8

def test_case_15():
    sol = Solution()
    assert sol.minPairSum([2, 3, 4, 4, 5, 6]) == 8

