# Test suite for wrong_hard_014  (slug: maximum-performance-of-a-team)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_014.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60

def test_case_2():
    sol = Solution()
    assert sol.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3) == 68

def test_case_3():
    sol = Solution()
    assert sol.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4) == 72

def test_case_4():
    sol = Solution()
    assert sol.maxPerformance(0, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60

def test_case_5():
    sol = Solution()
    assert sol.maxPerformance(1, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60

def test_case_6():
    sol = Solution()
    assert sol.maxPerformance(5, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60

def test_case_7():
    sol = Solution()
    assert sol.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60

def test_case_8():
    sol = Solution()
    assert sol.maxPerformance(7, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60

def test_case_9():
    sol = Solution()
    assert sol.maxPerformance(12, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60

def test_case_10():
    sol = Solution()
    assert sol.maxPerformance(16, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60

def test_case_11():
    sol = Solution()
    assert sol.maxPerformance(-1, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60

def test_case_12():
    sol = Solution()
    assert sol.maxPerformance(6, [], [5, 4, 3, 9, 7, 2], 2) == 0

def test_case_13():
    sol = Solution()
    assert sol.maxPerformance(6, [2], [5, 4, 3, 9, 7, 2], 2) == 10

def test_case_14():
    sol = Solution()
    assert sol.maxPerformance(6, [1, 2, 3, 5, 8, 10], [5, 4, 3, 9, 7, 2], 2) == 91

def test_case_15():
    sol = Solution()
    assert sol.maxPerformance(6, [10, 8, 5, 3, 2, 1], [5, 4, 3, 9, 7, 2], 2) == 72

