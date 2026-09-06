# Auto-generated test for wrong_hard_462  (slug: median-of-two-sorted-arrays)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_462.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.findMedianSortedArrays([1,3], [2])
    assert result == 2.00000

def test_case_2():
    sol = Solution()
    result = sol.findMedianSortedArrays([1,2], [3,4])
    assert result == 2.50000

