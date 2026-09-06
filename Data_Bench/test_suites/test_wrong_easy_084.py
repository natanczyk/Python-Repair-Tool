# Test suite for wrong_easy_084  (slug: nim-game)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_084.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.canWinNim(4) == False

def test_case_2():
    sol = Solution()
    assert sol.canWinNim(1) == True

def test_case_3():
    sol = Solution()
    assert sol.canWinNim(2) == True

def test_case_4():
    sol = Solution()
    assert sol.canWinNim(0) == False

def test_case_5():
    sol = Solution()
    assert sol.canWinNim(1) == True

def test_case_6():
    sol = Solution()
    assert sol.canWinNim(3) == True

def test_case_7():
    sol = Solution()
    assert sol.canWinNim(4) == False

def test_case_8():
    sol = Solution()
    assert sol.canWinNim(5) == True

def test_case_9():
    sol = Solution()
    assert sol.canWinNim(8) == False

def test_case_10():
    sol = Solution()
    assert sol.canWinNim(14) == True

def test_case_11():
    sol = Solution()
    assert sol.canWinNim(-1) == True

def test_case_12():
    sol = Solution()
    assert sol.canWinNim(0) == False

def test_case_13():
    sol = Solution()
    assert sol.canWinNim(1) == True

def test_case_14():
    sol = Solution()
    assert sol.canWinNim(2) == True

def test_case_15():
    sol = Solution()
    assert sol.canWinNim(11) == True

