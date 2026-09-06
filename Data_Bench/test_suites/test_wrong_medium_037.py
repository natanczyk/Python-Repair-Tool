# Auto-generated test for wrong_medium_037  (slug: all-elements-in-two-binary-search-trees)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_037.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.getAllElements([2,1,4], [1,0,3])
    assert result == [0,1,1,2,3,4]

def test_case_2():
    sol = Solution()
    result = sol.getAllElements([1,None,8], [8,1])
    assert result == [1,1,8,8]

