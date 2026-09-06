# Auto-generated test for wrong_easy_028  (slug: binary-tree-inorder-traversal)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_028.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.inorderTraversal([1,None,2,3])
    assert result == [1,3,2]

def test_case_2():
    sol = Solution()
    result = sol.inorderTraversal([])
    assert result == []

def test_case_3():
    sol = Solution()
    result = sol.inorderTraversal([1])
    assert result == [1]

