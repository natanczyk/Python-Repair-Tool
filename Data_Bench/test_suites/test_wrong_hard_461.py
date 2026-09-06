# Auto-generated test for wrong_hard_461  (slug: maximum-elegance-of-a-k-length-subsequence)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_461.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.findMaximumElegance([[3,2],[5,1],[10,1]], 2)
    assert result == 17

def test_case_2():
    sol = Solution()
    result = sol.findMaximumElegance([[3,1],[3,1],[2,2],[5,3]], 3)
    assert result == 19

def test_case_3():
    sol = Solution()
    result = sol.findMaximumElegance([[1,1],[2,1],[3,1]], 3)
    assert result == 7

