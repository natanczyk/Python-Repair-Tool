# Auto-generated test for wrong_medium_121  (slug: find-bottom-left-tree-value)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_121.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.findBottomLeftValue([2,1,3])
    assert result == 1

def test_case_2():
    sol = Solution()
    result = sol.findBottomLeftValue([1,2,3,4,None,5,6,None,None,7])
    assert result == 7

