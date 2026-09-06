# Test suite for wrong_hard_062  (slug: maximum-elegance-of-a-k-length-subsequence)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_062.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.findMaximumElegance([[3, 2], [5, 1], [10, 1]], 2) == 17

def test_case_2():
    sol = Solution()
    assert sol.findMaximumElegance([[3, 1], [3, 1], [2, 2], [5, 3]], 3) == 19

def test_case_3():
    sol = Solution()
    assert sol.findMaximumElegance([[1, 1], [2, 1], [3, 1]], 3) == 7

def test_case_4():
    sol = Solution()
    assert sol.findMaximumElegance([[0, 0], [0, 0], [0, 0]], 2) == 1

def test_case_5():
    sol = Solution()
    assert sol.findMaximumElegance([[1, 1], [1, 1], [1, 1]], 2) == 3

def test_case_6():
    sol = Solution()
    assert sol.findMaximumElegance([[2, 3], [1, 5], [1, 10]], 2) == 7

def test_case_7():
    sol = Solution()
    assert sol.findMaximumElegance([[10, 1], [5, 1], [3, 2]], 2) == 17

def test_case_8():
    sol = Solution()
    assert sol.findMaximumElegance([[3, 2], [5, 1], [10, 1]], 0) == 11

def test_case_9():
    sol = Solution()
    assert sol.findMaximumElegance([[3, 2], [5, 1], [10, 1]], 1) == 11

def test_case_10():
    sol = Solution()
    assert sol.findMaximumElegance([[3, 2], [5, 1], [10, 1]], 2) == 17

def test_case_11():
    sol = Solution()
    assert sol.findMaximumElegance([[3, 2], [5, 1], [10, 1]], 3) == 22

def test_case_12():
    sol = Solution()
    assert sol.findMaximumElegance([[3, 2], [5, 1], [10, 1]], 4) == -1

def test_case_13():
    sol = Solution()
    assert sol.findMaximumElegance([[3, 2], [5, 1], [10, 1]], 12) == -1

def test_case_14():
    sol = Solution()
    assert sol.findMaximumElegance([[3, 2], [5, 1], [10, 1]], -1) == 1

def test_case_15():
    sol = Solution()
    assert sol.findMaximumElegance([[0, 0], [0, 0], [0, 0], [0, 0]], 3) == 1

