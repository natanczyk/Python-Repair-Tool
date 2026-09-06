# Test suite for wrong_medium_295  (slug: koko-eating-bananas)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_295.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.minEatingSpeed([0, 0, 0, 0], 8) == 1

def test_case_2():
    sol = Solution()
    assert sol.minEatingSpeed([1, 1, 1, 1], 8) == 1

def test_case_3():
    sol = Solution()
    assert sol.minEatingSpeed([0, 0, 0, 0, 0], 5) == 1

def test_case_4():
    sol = Solution()
    assert sol.minEatingSpeed([1, 1, 1, 1, 1], 5) == 1

def test_case_5():
    sol = Solution()
    assert sol.minEatingSpeed([0, 0, 0, 0, 0], 6) == 1

def test_case_6():
    sol = Solution()
    assert sol.minEatingSpeed([1, 1, 1, 1, 1], 6) == 1

