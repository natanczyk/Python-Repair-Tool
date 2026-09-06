# Test suite for wrong_easy_165  (slug: rank-transform-of-an-array)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_165.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]

def test_case_2():
    sol = Solution()
    assert sol.arrayRankTransform([100, 100, 100]) == [1, 1, 1]

def test_case_3():
    sol = Solution()
    assert sol.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]) == [5, 3, 4, 2, 8, 6, 7, 1, 3]

def test_case_4():
    sol = Solution()
    assert sol.arrayRankTransform([]) == []

def test_case_5():
    sol = Solution()
    assert sol.arrayRankTransform([40]) == [1]

def test_case_6():
    sol = Solution()
    assert sol.arrayRankTransform([10, 20, 30, 40]) == [1, 2, 3, 4]

def test_case_7():
    sol = Solution()
    assert sol.arrayRankTransform([40, 30, 20, 10]) == [4, 3, 2, 1]

def test_case_8():
    sol = Solution()
    assert sol.arrayRankTransform([30, 20, 10, 40]) == [3, 2, 1, 4]

def test_case_9():
    sol = Solution()
    assert sol.arrayRankTransform([40, 10, 20, 30, 0]) == [5, 2, 3, 4, 1]

def test_case_10():
    sol = Solution()
    assert sol.arrayRankTransform([0, 0, 0, 0]) == [1, 1, 1, 1]

def test_case_11():
    sol = Solution()
    assert sol.arrayRankTransform([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_case_12():
    sol = Solution()
    assert sol.arrayRankTransform([41, 11, 21, 31]) == [4, 1, 2, 3]

def test_case_13():
    sol = Solution()
    assert sol.arrayRankTransform([39, 9, 19, 29]) == [4, 1, 2, 3]

def test_case_14():
    sol = Solution()
    assert sol.arrayRankTransform([40, 10, 20, 30, 40, 10, 20, 30]) == [4, 1, 2, 3, 4, 1, 2, 3]

def test_case_15():
    sol = Solution()
    assert sol.arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]

