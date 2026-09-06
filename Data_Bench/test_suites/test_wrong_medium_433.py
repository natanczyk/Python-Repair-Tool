# Test suite for wrong_medium_433  (slug: satisfiability-of-equality-equations)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_433.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.equationsPossible(['a==b', 'b!=a']) == False

def test_case_2():
    sol = Solution()
    assert sol.equationsPossible(['b==a', 'a==b']) == True

def test_case_3():
    sol = Solution()
    assert sol.equationsPossible([]) == True

def test_case_4():
    sol = Solution()
    assert sol.equationsPossible(['a==b']) == True

def test_case_5():
    sol = Solution()
    assert sol.equationsPossible(['a==b', 'b!=a']) == False

def test_case_6():
    sol = Solution()
    assert sol.equationsPossible(['b!=a', 'a==b']) == False

def test_case_7():
    sol = Solution()
    assert sol.equationsPossible([]) == True

def test_case_8():
    sol = Solution()
    assert sol.equationsPossible(['b==a']) == True

def test_case_9():
    sol = Solution()
    assert sol.equationsPossible(['a==b', 'b==a']) == True

def test_case_10():
    sol = Solution()
    assert sol.equationsPossible(['a==b', 'b==a']) == True

