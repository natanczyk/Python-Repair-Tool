# Test suite for wrong_medium_544  (slug: node-with-highest-edge-score)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_544.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.edgeScore([1, 0, 0, 0, 0, 7, 7, 5]) == 7

def test_case_2():
    sol = Solution()
    assert sol.edgeScore([2, 0, 0, 2]) == 0

def test_case_3():
    sol = Solution()
    assert sol.edgeScore([]) == 0

def test_case_4():
    sol = Solution()
    assert sol.edgeScore([0, 0, 0, 0, 1, 5, 7, 7]) == 7

def test_case_5():
    sol = Solution()
    assert sol.edgeScore([7, 7, 5, 1, 0, 0, 0, 0]) == 0

def test_case_6():
    sol = Solution()
    assert sol.edgeScore([5, 7, 7, 0, 0, 0, 0, 1]) == 0

def test_case_7():
    sol = Solution()
    assert sol.edgeScore([1, 0, 0, 0, 0, 7, 7, 5, 0]) == 0

def test_case_8():
    sol = Solution()
    assert sol.edgeScore([0, 0, 0, 0, 0, 0, 0, 0]) == 0

def test_case_9():
    sol = Solution()
    assert sol.edgeScore([1, 1, 1, 1, 1, 1, 1, 1]) == 1

def test_case_10():
    sol = Solution()
    assert sol.edgeScore([0, -1, -1, -1, -1, 6, 6, 4]) == 6

def test_case_11():
    sol = Solution()
    assert sol.edgeScore([1, 0, 0, 0, 0, 7, 7, 5, 1, 0, 0, 0, 0, 7, 7, 5]) == 0

def test_case_12():
    sol = Solution()
    assert sol.edgeScore([]) == 0

def test_case_13():
    sol = Solution()
    assert sol.edgeScore([0, 0, 2, 2]) == 2

def test_case_14():
    sol = Solution()
    assert sol.edgeScore([2, 2, 0, 0]) == 0

def test_case_15():
    sol = Solution()
    assert sol.edgeScore([2, 0, 0, 2]) == 0

