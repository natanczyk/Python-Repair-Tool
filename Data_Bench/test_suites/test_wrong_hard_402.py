# Test suite for wrong_hard_402  (slug: sliding-window-median)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_402.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.medianSlidingWindow([], 3) == []

def test_case_2():
    sol = Solution()
    assert sol.medianSlidingWindow([], 3) == []

