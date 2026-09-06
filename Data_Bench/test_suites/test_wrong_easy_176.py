# Test suite for wrong_easy_176  (slug: minimum-distance-to-the-target-element)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_176.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.getMinDistance([1, 2, 3, 4, 5], 5, 3) == 1

def test_case_2():
    sol = Solution()
    assert sol.getMinDistance([1], 1, 0) == 0

def test_case_3():
    sol = Solution()
    assert sol.getMinDistance([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0) == 0

def test_case_4():
    sol = Solution()
    assert sol.getMinDistance([1, 2, 3, 4, 5], 5, 3) == 1

def test_case_5():
    sol = Solution()
    assert sol.getMinDistance([5, 4, 3, 2, 1], 5, 3) == 3

def test_case_6():
    sol = Solution()
    assert sol.getMinDistance([1, 2, 3, 4, 5, 0], 5, 3) == 1

def test_case_7():
    sol = Solution()
    assert sol.getMinDistance([0, 0, 0, 0, 0], 5, 3) == 5

def test_case_8():
    sol = Solution()
    assert sol.getMinDistance([1, 1, 1, 1, 1], 5, 3) == 5

def test_case_9():
    sol = Solution()
    assert sol.getMinDistance([2, 3, 4, 5, 6], 5, 3) == 0

def test_case_10():
    sol = Solution()
    assert sol.getMinDistance([0, 1, 2, 3, 4], 5, 3) == 5

def test_case_11():
    sol = Solution()
    assert sol.getMinDistance([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 5, 3) == 1

def test_case_12():
    sol = Solution()
    assert sol.getMinDistance([1, 2, 3, 4, 5], 0, 3) == 5

def test_case_13():
    sol = Solution()
    assert sol.getMinDistance([1, 2, 3, 4, 5], 1, 3) == 3

def test_case_14():
    sol = Solution()
    assert sol.getMinDistance([1, 2, 3, 4, 5], 4, 3) == 0

def test_case_15():
    sol = Solution()
    assert sol.getMinDistance([1, 2, 3, 4, 5], 5, 3) == 1

