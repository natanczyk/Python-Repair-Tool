# Auto-generated test for wrong_easy_107  (slug: linked-list-cycle)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_107.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.hasCycle([3,2,0,-4])
    assert result == True

def test_case_2():
    sol = Solution()
    result = sol.hasCycle([1,2])
    assert result == True

def test_case_3():
    sol = Solution()
    result = sol.hasCycle([1])
    assert result == False

