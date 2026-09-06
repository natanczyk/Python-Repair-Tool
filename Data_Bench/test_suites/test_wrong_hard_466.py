# Auto-generated test for wrong_hard_466  (slug: check-if-string-is-transformable-with-substring-sort-operations)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_466.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.isTransformable("84532", "34852")
    assert result == True

def test_case_2():
    sol = Solution()
    result = sol.isTransformable("34521", "23415")
    assert result == True

def test_case_3():
    sol = Solution()
    result = sol.isTransformable("12345", "12435")
    assert result == False

