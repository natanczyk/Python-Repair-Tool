# Auto-generated test for wrong_hard_015  (slug: merge-k-sorted-lists)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_015.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.mergeKLists([[1,4,5],[1,3,4],[2,6]])
    assert result == [1,1,2,3,4,4,5,6]

def test_case_2():
    sol = Solution()
    result = sol.mergeKLists([])
    assert result == []

def test_case_3():
    sol = Solution()
    result = sol.mergeKLists([[]])
    assert result == []

