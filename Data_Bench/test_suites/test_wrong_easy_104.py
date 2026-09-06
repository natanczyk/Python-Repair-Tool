# Auto-generated test for wrong_easy_104  (slug: maximum-depth-of-binary-tree)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_104.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.maxDepth([3,9,20,None,None,15,7])
    assert result == 3

def test_case_2():
    sol = Solution()
    result = sol.maxDepth([1,None,2])
    assert result == 2

