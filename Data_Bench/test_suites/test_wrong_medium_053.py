# Auto-generated test for wrong_medium_053  (slug: remove-duplicates-from-sorted-array-ii)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_053.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.removeDuplicates([1,1,1,2,2,3])
    assert result == 5, nums = [1,1,2,2,3,_]

def test_case_2():
    sol = Solution()
    result = sol.removeDuplicates([0,0,1,1,1,1,2,3,3])
    assert result == 7, nums = [0,0,1,1,2,3,3,_,_]

