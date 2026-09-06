# Auto-generated test for wrong_medium_019  (slug: binary-tree-level-order-traversal-ii)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_019.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.levelOrderBottom([3,9,20,None,None,15,7])
    assert result == [[15,7],[9,20],[3]]

def test_case_2():
    sol = Solution()
    result = sol.levelOrderBottom([1])
    assert result == [[1]]

def test_case_3():
    sol = Solution()
    result = sol.levelOrderBottom([])
    assert result == []

