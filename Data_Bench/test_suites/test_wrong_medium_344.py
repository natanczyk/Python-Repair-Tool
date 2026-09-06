# Test suite for wrong_medium_344  (slug: maximum-gap)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_344.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.maximumGap([3, 6, 9, 1]) == 3

def test_case_2():
    sol = Solution()
    assert sol.maximumGap([10]) == 0

def test_case_3():
    sol = Solution()
    assert sol.maximumGap([]) == 0

def test_case_4():
    sol = Solution()
    assert sol.maximumGap([3]) == 0

def test_case_5():
    sol = Solution()
    assert sol.maximumGap([1, 3, 6, 9]) == 3

def test_case_6():
    sol = Solution()
    assert sol.maximumGap([9, 6, 3, 1]) == 3

def test_case_7():
    sol = Solution()
    assert sol.maximumGap([1, 9, 6, 3]) == 3

def test_case_8():
    sol = Solution()
    assert sol.maximumGap([3, 6, 9, 1, 0]) == 3

def test_case_9():
    sol = Solution()
    assert sol.maximumGap([0, 0, 0, 0]) == 0

def test_case_10():
    sol = Solution()
    assert sol.maximumGap([1, 1, 1, 1]) == 0

def test_case_11():
    sol = Solution()
    assert sol.maximumGap([4, 7, 10, 2]) == 3

def test_case_12():
    sol = Solution()
    assert sol.maximumGap([2, 5, 8, 0]) == 3

def test_case_13():
    sol = Solution()
    assert sol.maximumGap([3, 6, 9, 1, 3, 6, 9, 1]) == 3

def test_case_14():
    sol = Solution()
    assert sol.maximumGap([9, 3, 6, 1]) == 3

def test_case_15():
    sol = Solution()
    assert sol.maximumGap([]) == 0

