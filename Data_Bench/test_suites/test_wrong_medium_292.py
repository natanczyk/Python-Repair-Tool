# Test suite for wrong_medium_292  (slug: minimum-fuel-cost-to-report-to-the-capital)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_292.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5) == 3

def test_case_2():
    sol = Solution()
    assert sol.minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2) == 7

def test_case_3():
    sol = Solution()
    assert sol.minimumFuelCost([], 1) == 0

def test_case_4():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 0], [0, 0], [0, 0]], 5) == 0

def test_case_5():
    sol = Solution()
    assert sol.minimumFuelCost([[1, 1], [1, 1], [1, 1]], 5) == 0

def test_case_6():
    sol = Solution()
    assert sol.minimumFuelCost([[1, 0], [2, 0], [3, 0]], 5) == 3

def test_case_7():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 3], [0, 2], [0, 1]], 5) == 3

def test_case_8():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 1) == 3

def test_case_9():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 4) == 3

def test_case_10():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5) == 3

def test_case_11():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 6) == 3

def test_case_12():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 10) == 3

def test_case_13():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 15) == 3

def test_case_14():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 1], [0, 2], [0, 3]], -1) == -3

def test_case_15():
    sol = Solution()
    assert sol.minimumFuelCost([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], 2) == 0

