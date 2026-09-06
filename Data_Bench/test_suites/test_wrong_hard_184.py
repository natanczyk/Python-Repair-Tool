# Test suite for wrong_hard_184  (slug: maximum-sum-queries)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_184.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.maximumSumQueries([4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [6, 10, 7]

def test_case_2():
    sol = Solution()
    assert sol.maximumSumQueries([3, 2, 5], [2, 3, 4], [[4, 4], [3, 2], [1, 1]]) == [9, 9, 9]

def test_case_3():
    sol = Solution()
    assert sol.maximumSumQueries([2, 1], [2, 3], [[3, 3]]) == [-1]

def test_case_4():
    sol = Solution()
    assert sol.maximumSumQueries([4], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [6, -1, -1]

def test_case_5():
    sol = Solution()
    assert sol.maximumSumQueries([1, 2, 3, 4], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [9, 12, 12]

def test_case_6():
    sol = Solution()
    assert sol.maximumSumQueries([4, 3, 2, 1], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [6, 11, 11]

def test_case_7():
    sol = Solution()
    assert sol.maximumSumQueries([2, 1, 3, 4], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [9, 12, 12]

def test_case_8():
    sol = Solution()
    assert sol.maximumSumQueries([0, 0, 0, 0], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [-1, -1, -1]

def test_case_9():
    sol = Solution()
    assert sol.maximumSumQueries([1, 1, 1, 1], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [-1, 10, -1]

def test_case_10():
    sol = Solution()
    assert sol.maximumSumQueries([5, 4, 2, 3], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [8, 11, 11]

def test_case_11():
    sol = Solution()
    assert sol.maximumSumQueries([3, 2, 0, 1], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [-1, 6, -1]

def test_case_12():
    sol = Solution()
    assert sol.maximumSumQueries([4, 3, 1, 2], [2, 4, 5, 9], [[4, 1], [1, 3], [2, 5]]) == [6, 11, 11]

def test_case_13():
    sol = Solution()
    assert sol.maximumSumQueries([4, 3, 1, 2], [9, 5, 4, 2], [[4, 1], [1, 3], [2, 5]]) == [13, 13, 13]

def test_case_14():
    sol = Solution()
    assert sol.maximumSumQueries([4, 3, 1, 2], [5, 9, 4, 2], [[4, 1], [1, 3], [2, 5]]) == [9, 12, 12]

def test_case_15():
    sol = Solution()
    assert sol.maximumSumQueries([4, 3, 1, 2], [2, 4, 9, 5, 0], [[4, 1], [1, 3], [2, 5]]) == [6, 10, 7]

