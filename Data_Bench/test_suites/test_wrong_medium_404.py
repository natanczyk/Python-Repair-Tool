# Auto-generated test for wrong_medium_404  (slug: construct-binary-tree-from-inorder-and-postorder-traversal)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_404.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.buildTree([9,3,15,20,7], [9,15,7,20,3])
    assert result == [3,9,20,None,None,15,7]

def test_case_2():
    sol = Solution()
    result = sol.buildTree([-1], [-1])
    assert result == [-1]

