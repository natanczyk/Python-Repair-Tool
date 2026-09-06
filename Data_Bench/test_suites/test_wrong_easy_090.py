# Auto-generated test for wrong_easy_090  (slug: increasing-order-search-tree)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_090.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.increasingBST([5,3,6,2,4,None,8,1,None,None,None,7,9])
    assert result == [1,None,2,None,3,None,4,None,5,None,6,None,7,None,8,None,9]

def test_case_2():
    sol = Solution()
    result = sol.increasingBST([5,1,7])
    assert result == [1,None,5,None,7]

