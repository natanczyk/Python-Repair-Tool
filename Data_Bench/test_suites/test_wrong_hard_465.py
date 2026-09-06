# Auto-generated test for wrong_hard_465  (slug: maximize-the-minimum-powered-city)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_465.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.maxPower([1,2,4,5,0], 1, 2)
    assert result == 5

def test_case_2():
    sol = Solution()
    result = sol.maxPower([4,4,4,4], 0, 3)
    assert result == 4

