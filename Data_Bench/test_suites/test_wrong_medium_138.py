# Auto-generated test for wrong_medium_138  (slug: kth-largest-sum-in-a-binary-tree)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_138.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.kthLargestLevelSum([5,8,9,2,1,3,7,4,6], 2)
    assert result == 13

def test_case_2():
    sol = Solution()
    result = sol.kthLargestLevelSum([1,2,None,3], 1)
    assert result == 3

