# Test suite for wrong_easy_228  (slug: two-furthest-houses-with-different-colors)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_228.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.maxDistance([1, 1, 1, 6, 1, 1, 1]) == 3

def test_case_2():
    sol = Solution()
    assert sol.maxDistance([1, 8, 3, 8, 3]) == 4

def test_case_3():
    sol = Solution()
    assert sol.maxDistance([0, 1]) == 1

def test_case_4():
    sol = Solution()
    assert sol.maxDistance([]) == 0

def test_case_5():
    sol = Solution()
    assert sol.maxDistance([1]) == 0

def test_case_6():
    sol = Solution()
    assert sol.maxDistance([1, 1, 1, 1, 1, 1, 6]) == 6

def test_case_7():
    sol = Solution()
    assert sol.maxDistance([6, 1, 1, 1, 1, 1, 1]) == 6

def test_case_8():
    sol = Solution()
    assert sol.maxDistance([1, 1, 1, 6, 1, 1, 1]) == 3

def test_case_9():
    sol = Solution()
    assert sol.maxDistance([1, 1, 1, 6, 1, 1, 1, 0]) == 7

def test_case_10():
    sol = Solution()
    assert sol.maxDistance([0, 0, 0, 0, 0, 0, 0]) == 0

def test_case_11():
    sol = Solution()
    assert sol.maxDistance([1, 1, 1, 1, 1, 1, 1]) == 0

def test_case_12():
    sol = Solution()
    assert sol.maxDistance([2, 2, 2, 7, 2, 2, 2]) == 3

def test_case_13():
    sol = Solution()
    assert sol.maxDistance([0, 0, 0, 5, 0, 0, 0]) == 3

def test_case_14():
    sol = Solution()
    assert sol.maxDistance([1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1]) == 10

def test_case_15():
    sol = Solution()
    assert sol.maxDistance([1, 6]) == 1

