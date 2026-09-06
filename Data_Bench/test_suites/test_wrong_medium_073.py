# Auto-generated test for wrong_medium_073  (slug: convert-sorted-list-to-binary-search-tree)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_073.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.sortedListToBST([-10,-3,0,5,9])
    assert result == [0,-3,9,-10,None,5]

def test_case_2():
    sol = Solution()
    result = sol.sortedListToBST([])
    assert result == []

