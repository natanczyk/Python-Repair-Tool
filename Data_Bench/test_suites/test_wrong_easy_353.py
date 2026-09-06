# Test suite for wrong_easy_353  (slug: n-th-tribonacci-number)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_353.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.tribonacci(4) == 4

def test_case_2():
    sol = Solution()
    assert sol.tribonacci(25) == 1389537

def test_case_3():
    sol = Solution()
    assert sol.tribonacci(0) == 0

def test_case_4():
    sol = Solution()
    assert sol.tribonacci(1) == 1

def test_case_5():
    sol = Solution()
    assert sol.tribonacci(3) == 2

def test_case_6():
    sol = Solution()
    assert sol.tribonacci(4) == 4

def test_case_7():
    sol = Solution()
    assert sol.tribonacci(5) == 7

def test_case_8():
    sol = Solution()
    assert sol.tribonacci(8) == 44

def test_case_9():
    sol = Solution()
    assert sol.tribonacci(14) == 1705

def test_case_10():
    sol = Solution()
    assert sol.tribonacci(-1) == 1

def test_case_11():
    sol = Solution()
    assert sol.tribonacci(0) == 0

def test_case_12():
    sol = Solution()
    assert sol.tribonacci(1) == 1

def test_case_13():
    sol = Solution()
    assert sol.tribonacci(35) == 615693474

def test_case_14():
    sol = Solution()
    assert sol.tribonacci(50) == 5742568741225

def test_case_15():
    sol = Solution()
    assert sol.tribonacci(24) == 755476

