# Auto-generated test for wrong_easy_085  (slug: remove-linked-list-elements)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_085.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.removeElements([1,2,6,3,4,5,6], 6)
    assert result == [1,2,3,4,5]

def test_case_2():
    sol = Solution()
    result = sol.removeElements([], 1)
    assert result == []

def test_case_3():
    sol = Solution()
    result = sol.removeElements([7,7,7,7], 7)
    assert result == []

