# Auto-generated test for wrong_medium_056  (slug: powerful-integers)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_056.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.powerfulIntegers(2, 3, 10)
    assert result == [2,3,4,5,7,9,10]

def test_case_2():
    sol = Solution()
    result = sol.powerfulIntegers(3, 5, 15)
    assert result == [2,4,6,8,10,14]

