# Auto-generated test for wrong_medium_065  (slug: amount-of-time-for-binary-tree-to-be-infected)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_065.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.amountOfTime([1,5,3,None,4,10,6,9,2], 3)
    assert result == 4

def test_case_2():
    sol = Solution()
    result = sol.amountOfTime([1], 1)
    assert result == 0

