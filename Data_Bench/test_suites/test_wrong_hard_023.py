# Test suite for wrong_hard_023  (slug: check-if-point-is-reachable)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_023.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.isReachable(0, 9) == False

def test_case_2():
    sol = Solution()
    assert sol.isReachable(1, 9) == True

def test_case_3():
    sol = Solution()
    assert sol.isReachable(5, 9) == True

def test_case_4():
    sol = Solution()
    assert sol.isReachable(6, 9) == False

def test_case_5():
    sol = Solution()
    assert sol.isReachable(7, 9) == True

def test_case_6():
    sol = Solution()
    assert sol.isReachable(12, 9) == False

def test_case_7():
    sol = Solution()
    assert sol.isReachable(16, 9) == True

def test_case_8():
    sol = Solution()
    assert sol.isReachable(-1, 9) == True

def test_case_9():
    sol = Solution()
    assert sol.isReachable(6, 0) == False

def test_case_10():
    sol = Solution()
    assert sol.isReachable(6, 1) == True

def test_case_11():
    sol = Solution()
    assert sol.isReachable(6, 8) == True

def test_case_12():
    sol = Solution()
    assert sol.isReachable(6, 9) == False

def test_case_13():
    sol = Solution()
    assert sol.isReachable(6, 10) == True

def test_case_14():
    sol = Solution()
    assert sol.isReachable(6, 18) == False

def test_case_15():
    sol = Solution()
    assert sol.isReachable(6, 19) == True

