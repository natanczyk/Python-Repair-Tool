# Test suite for wrong_easy_011  (slug: delete-greatest-value-in-each-row)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_011.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.deleteGreatestValue([[], []]) == 8

def test_case_2():
    sol = Solution()
    assert sol.deleteGreatestValue([[]]) == 10

def test_case_3():
    sol = Solution()
    assert sol.deleteGreatestValue([[], []]) == 0

def test_case_4():
    sol = Solution()
    assert sol.deleteGreatestValue([[], []]) == 3

def test_case_5():
    sol = Solution()
    assert sol.deleteGreatestValue([[], []]) == 8

def test_case_6():
    sol = Solution()
    assert sol.deleteGreatestValue([[], []]) == 0

def test_case_7():
    sol = Solution()
    assert sol.deleteGreatestValue([[]]) == 0

def test_case_8():
    sol = Solution()
    assert sol.deleteGreatestValue([[]]) == 1

def test_case_9():
    sol = Solution()
    assert sol.deleteGreatestValue([[]]) == 10

def test_case_10():
    sol = Solution()
    assert sol.deleteGreatestValue([[]]) == 0

