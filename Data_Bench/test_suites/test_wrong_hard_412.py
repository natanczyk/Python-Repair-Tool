# Auto-generated test for wrong_hard_412  (slug: maximize-number-of-nice-divisors)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_412.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.maxNiceDivisors(5)
    assert result == 6

def test_case_2():
    sol = Solution()
    result = sol.maxNiceDivisors(8)
    assert result == 18

