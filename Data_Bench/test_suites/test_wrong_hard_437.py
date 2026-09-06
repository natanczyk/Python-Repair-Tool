# Auto-generated test for wrong_hard_437  (slug: scramble-string)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_437.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.isScramble("great", "rgeat")
    assert result == True

def test_case_2():
    sol = Solution()
    result = sol.isScramble("abcde", "caebd")
    assert result == False

def test_case_3():
    sol = Solution()
    result = sol.isScramble("a", "a")
    assert result == True

