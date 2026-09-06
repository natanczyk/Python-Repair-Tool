# Auto-generated test for wrong_medium_082  (slug: maximum-product-of-splitted-binary-tree)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_082.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.maxProduct([1,2,3,4,5,6])
    assert result == 110

def test_case_2():
    sol = Solution()
    result = sol.maxProduct([1,None,2,3,4,None,None,5,6])
    assert result == 90

