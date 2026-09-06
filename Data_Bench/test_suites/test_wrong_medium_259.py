# Auto-generated test for wrong_medium_259  (slug: maximum-difference-between-node-and-ancestor)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_259.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.maxAncestorDiff([8,3,10,1,6,None,14,None,None,4,7,13])
    assert result == 7

def test_case_2():
    sol = Solution()
    result = sol.maxAncestorDiff([1,None,2,None,0,3])
    assert result == 3

