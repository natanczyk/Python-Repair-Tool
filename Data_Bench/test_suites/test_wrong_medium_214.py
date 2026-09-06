# Test suite for wrong_medium_214  (slug: kth-largest-element-in-an-array)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_214.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

def test_case_2():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

def test_case_3():
    sol = Solution()
    assert sol.findKthLargest([1, 2, 3, 4, 5, 6], 2) == 5

def test_case_4():
    sol = Solution()
    assert sol.findKthLargest([6, 5, 4, 3, 2, 1], 2) == 5

def test_case_5():
    sol = Solution()
    assert sol.findKthLargest([4, 6, 5, 1, 2, 3], 2) == 5

def test_case_6():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4, 0], 2) == 5

def test_case_7():
    sol = Solution()
    assert sol.findKthLargest([0, 0, 0, 0, 0, 0], 2) == 0

def test_case_8():
    sol = Solution()
    assert sol.findKthLargest([1, 1, 1, 1, 1, 1], 2) == 1

def test_case_9():
    sol = Solution()
    assert sol.findKthLargest([4, 3, 2, 6, 7, 5], 2) == 6

def test_case_10():
    sol = Solution()
    assert sol.findKthLargest([2, 1, 0, 4, 5, 3], 2) == 4

def test_case_11():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4, 3, 2, 1, 5, 6, 4], 2) == 6

def test_case_12():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 0) == 1

def test_case_13():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 1) == 6

def test_case_14():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

def test_case_15():
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 3) == 4

