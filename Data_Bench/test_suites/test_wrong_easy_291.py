# Test suite for wrong_easy_291  (slug: self-dividing-numbers)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_291.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.selfDividingNumbers(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def test_case_2():
    sol = Solution()
    assert sol.selfDividingNumbers(47, 85) == [48, 55, 66, 77]

def test_case_3():
    sol = Solution()
    assert sol.selfDividingNumbers(0, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def test_case_4():
    sol = Solution()
    assert sol.selfDividingNumbers(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def test_case_5():
    sol = Solution()
    assert sol.selfDividingNumbers(2, 22) == [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def test_case_6():
    sol = Solution()
    assert sol.selfDividingNumbers(11, 22) == [11, 12, 15, 22]

def test_case_7():
    sol = Solution()
    assert sol.selfDividingNumbers(1, 0) == []

def test_case_8():
    sol = Solution()
    assert sol.selfDividingNumbers(1, 1) == [1]

def test_case_9():
    sol = Solution()
    assert sol.selfDividingNumbers(1, 32) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24]

def test_case_10():
    sol = Solution()
    assert sol.selfDividingNumbers(1, 44) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44]

def test_case_11():
    sol = Solution()
    assert sol.selfDividingNumbers(1, 21) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]

def test_case_12():
    sol = Solution()
    assert sol.selfDividingNumbers(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def test_case_13():
    sol = Solution()
    assert sol.selfDividingNumbers(1, 23) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def test_case_14():
    sol = Solution()
    assert sol.selfDividingNumbers(1, -1) == []

def test_case_15():
    sol = Solution()
    assert sol.selfDividingNumbers(0, 85) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77]

