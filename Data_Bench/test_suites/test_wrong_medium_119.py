# Auto-generated test for wrong_medium_119  (slug: split-linked-list-in-parts)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_119.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.splitListToParts([1,2,3], 5)
    assert result == [[1],[2],[3],[],[]]

def test_case_2():
    sol = Solution()
    result = sol.splitListToParts([1,2,3,4,5,6,7,8,9,10], 3)
    assert result == [[1,2,3,4],[5,6,7],[8,9,10]]

