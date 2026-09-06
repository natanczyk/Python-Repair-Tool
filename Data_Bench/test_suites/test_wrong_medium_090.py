# Test suite for wrong_medium_090  (slug: the-kth-factor-of-n)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_090.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.kthFactor(0, 3) == -1

def test_case_2():
    sol = Solution()
    assert sol.kthFactor(1, 3) == -1

def test_case_3():
    sol = Solution()
    assert sol.kthFactor(11, 3) == -1

def test_case_4():
    sol = Solution()
    assert sol.kthFactor(12, 3) == 3

def test_case_5():
    sol = Solution()
    assert sol.kthFactor(13, 3) == -1

def test_case_6():
    sol = Solution()
    assert sol.kthFactor(22, 3) == 11

def test_case_7():
    sol = Solution()
    assert sol.kthFactor(24, 3) == 3

def test_case_8():
    sol = Solution()
    assert sol.kthFactor(-1, 3) == -1

def test_case_9():
    sol = Solution()
    assert sol.kthFactor(12, 0) == -1

def test_case_10():
    sol = Solution()
    assert sol.kthFactor(12, 1) == 1

def test_case_11():
    sol = Solution()
    assert sol.kthFactor(12, 2) == 2

def test_case_12():
    sol = Solution()
    assert sol.kthFactor(12, 3) == 3

def test_case_13():
    sol = Solution()
    assert sol.kthFactor(12, 4) == 4

def test_case_14():
    sol = Solution()
    assert sol.kthFactor(12, 6) == 12

def test_case_15():
    sol = Solution()
    assert sol.kthFactor(12, 13) == -1

