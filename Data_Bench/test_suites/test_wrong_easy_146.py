# Test suite for wrong_easy_146  (slug: number-complement)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_146.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.findComplement(5) == 2

def test_case_2():
    sol = Solution()
    assert sol.findComplement(1) == 0

def test_case_3():
    sol = Solution()
    assert sol.findComplement(1) == 0

def test_case_4():
    sol = Solution()
    assert sol.findComplement(4) == 3

def test_case_5():
    sol = Solution()
    assert sol.findComplement(5) == 2

def test_case_6():
    sol = Solution()
    assert sol.findComplement(6) == 1

def test_case_7():
    sol = Solution()
    assert sol.findComplement(10) == 5

def test_case_8():
    sol = Solution()
    assert sol.findComplement(15) == 0

def test_case_9():
    sol = Solution()
    assert sol.findComplement(1) == 0

def test_case_10():
    sol = Solution()
    assert sol.findComplement(2) == 1

def test_case_11():
    sol = Solution()
    assert sol.findComplement(11) == 4

