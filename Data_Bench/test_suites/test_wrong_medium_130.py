# Auto-generated test for wrong_medium_130  (slug: linked-list-in-binary-tree)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_130.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.isSubPath([4,2,8], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
    assert result == True

def test_case_2():
    sol = Solution()
    result = sol.isSubPath([1,4,2,6], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
    assert result == True

def test_case_3():
    sol = Solution()
    result = sol.isSubPath([1,4,2,6,8], [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
    assert result == False

