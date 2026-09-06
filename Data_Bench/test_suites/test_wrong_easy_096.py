# Test suite for wrong_easy_096  (slug: calculate-money-in-leetcode-bank)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_096.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.totalMoney(4) == 10

def test_case_2():
    sol = Solution()
    assert sol.totalMoney(10) == 37

def test_case_3():
    sol = Solution()
    assert sol.totalMoney(20) == 96

def test_case_4():
    sol = Solution()
    assert sol.totalMoney(0) == 0

def test_case_5():
    sol = Solution()
    assert sol.totalMoney(1) == 1

def test_case_6():
    sol = Solution()
    assert sol.totalMoney(3) == 6

def test_case_7():
    sol = Solution()
    assert sol.totalMoney(4) == 10

def test_case_8():
    sol = Solution()
    assert sol.totalMoney(5) == 15

def test_case_9():
    sol = Solution()
    assert sol.totalMoney(8) == 30

def test_case_10():
    sol = Solution()
    assert sol.totalMoney(14) == 63

def test_case_11():
    sol = Solution()
    assert sol.totalMoney(-1) == 0

def test_case_12():
    sol = Solution()
    assert sol.totalMoney(0) == 0

def test_case_13():
    sol = Solution()
    assert sol.totalMoney(1) == 1

def test_case_14():
    sol = Solution()
    assert sol.totalMoney(9) == 33

def test_case_15():
    sol = Solution()
    assert sol.totalMoney(10) == 37

