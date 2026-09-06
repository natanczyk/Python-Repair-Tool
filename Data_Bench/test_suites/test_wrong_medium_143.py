# Auto-generated test for wrong_medium_143  (slug: construct-binary-tree-from-preorder-and-inorder-traversal)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_143.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
    assert result == [3,9,20,None,None,15,7]

def test_case_2():
    sol = Solution()
    result = sol.buildTree([-1], [-1])
    assert result == [-1]

