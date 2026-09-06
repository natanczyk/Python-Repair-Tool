# Test suite for wrong_medium_024  (slug: can-you-eat-your-favorite-candy-on-your-favorite-day)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_024.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.canEat([7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, True]

def test_case_2():
    sol = Solution()
    assert sol.canEat([5, 2, 6, 4, 1], [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]) == [False, True, True, False, False]

def test_case_3():
    sol = Solution()
    assert sol.canEat([3, 4, 5, 7, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, False]

def test_case_4():
    sol = Solution()
    assert sol.canEat([8, 7, 5, 4, 3], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, True]

def test_case_5():
    sol = Solution()
    assert sol.canEat([8, 3, 5, 4, 7], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, True]

def test_case_6():
    sol = Solution()
    assert sol.canEat([7, 4, 5, 3, 8, 0], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, True]

def test_case_7():
    sol = Solution()
    assert sol.canEat([0, 0, 0, 0, 0], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [False, False, False]

def test_case_8():
    sol = Solution()
    assert sol.canEat([1, 1, 1, 1, 1], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [False, True, False]

def test_case_9():
    sol = Solution()
    assert sol.canEat([8, 5, 6, 4, 9], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, True]

def test_case_10():
    sol = Solution()
    assert sol.canEat([6, 3, 4, 2, 7], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, False]

def test_case_11():
    sol = Solution()
    assert sol.canEat([7, 4, 5, 3, 8, 7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, True]

def test_case_12():
    sol = Solution()
    assert sol.canEat([7, 4, 5, 3, 8], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == [False, False, False]

def test_case_13():
    sol = Solution()
    assert sol.canEat([7, 4, 5, 3, 8], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == [False, False, False]

def test_case_14():
    sol = Solution()
    assert sol.canEat([7, 4, 5, 3, 8], [[2, 13, 1000000000], [4, 2, 4], [0, 2, 2]]) == [True, False, True]

def test_case_15():
    sol = Solution()
    assert sol.canEat([1, 2, 4, 5, 6], [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]) == [False, True, True, False, False]

