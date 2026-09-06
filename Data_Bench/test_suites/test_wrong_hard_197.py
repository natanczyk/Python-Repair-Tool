# Auto-generated test for wrong_hard_197  (slug: minimize-the-total-price-of-the-trips)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_197.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.minimumTotalPrice(4, [[0,1],[1,2],[1,3]], [2,2,10,6], [[0,3],[2,1],[2,3]])
    assert result == 23

def test_case_2():
    sol = Solution()
    result = sol.minimumTotalPrice(2, [[0,1]], [2,2], [[0,0]])
    assert result == 1

