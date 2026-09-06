# Auto-generated test for wrong_medium_006  (slug: smallest-string-starting-from-leaf)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_006.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.smallestFromLeaf([0,1,2,3,4,3,4])
    assert result == "dba"

def test_case_2():
    sol = Solution()
    result = sol.smallestFromLeaf([25,1,3,1,3,0,2])
    assert result == "adz"

def test_case_3():
    sol = Solution()
    result = sol.smallestFromLeaf([2,2,1,None,1,0,None,0])
    assert result == "abc"

