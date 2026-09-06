# Auto-generated test for wrong_easy_305  (slug: find-mode-in-binary-search-tree)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_305.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.findMode([1,None,2,2])
    assert result == [2]

def test_case_2():
    sol = Solution()
    result = sol.findMode([0])
    assert result == [0]

