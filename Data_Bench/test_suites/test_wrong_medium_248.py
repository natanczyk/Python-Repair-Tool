# Test suite for wrong_medium_248  (slug: count-good-numbers)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_248.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.countGoodNumbers(0) == 1

def test_case_2():
    sol = Solution()
    assert sol.countGoodNumbers(1) == 5

def test_case_3():
    sol = Solution()
    assert sol.countGoodNumbers(2) == 20

def test_case_4():
    sol = Solution()
    assert sol.countGoodNumbers(11) == 16000000

def test_case_5():
    sol = Solution()
    assert sol.countGoodNumbers(-1) == 250000002

def test_case_6():
    sol = Solution()
    assert sol.countGoodNumbers(0) == 1

def test_case_7():
    sol = Solution()
    assert sol.countGoodNumbers(1) == 5

def test_case_8():
    sol = Solution()
    assert sol.countGoodNumbers(3) == 100

def test_case_9():
    sol = Solution()
    assert sol.countGoodNumbers(4) == 400

def test_case_10():
    sol = Solution()
    assert sol.countGoodNumbers(5) == 2000

def test_case_11():
    sol = Solution()
    assert sol.countGoodNumbers(8) == 160000

def test_case_12():
    sol = Solution()
    assert sol.countGoodNumbers(14) == 279999993

def test_case_13():
    sol = Solution()
    assert sol.countGoodNumbers(-1) == 250000002

def test_case_14():
    sol = Solution()
    assert sol.countGoodNumbers(0) == 1

def test_case_15():
    sol = Solution()
    assert sol.countGoodNumbers(1) == 5

