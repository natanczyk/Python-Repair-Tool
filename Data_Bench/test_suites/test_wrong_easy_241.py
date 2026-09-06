# Test suite for wrong_easy_241  (slug: check-if-every-row-and-column-contains-all-numbers)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_241.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]) == True

def test_case_2():
    sol = Solution()
    assert sol.checkValid([[1, 1, 1], [1, 2, 3], [1, 2, 3]]) == False

def test_case_3():
    sol = Solution()
    assert sol.checkValid([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == False

def test_case_4():
    sol = Solution()
    assert sol.checkValid([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == False

def test_case_5():
    sol = Solution()
    assert sol.checkValid([[3, 2, 1], [2, 1, 3], [1, 3, 2]]) == True

def test_case_6():
    sol = Solution()
    assert sol.checkValid([[2, 3, 1], [3, 1, 2], [1, 2, 3]]) == True

def test_case_7():
    sol = Solution()
    assert sol.checkValid([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == False

def test_case_8():
    sol = Solution()
    assert sol.checkValid([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == False

def test_case_9():
    sol = Solution()
    assert sol.checkValid([[1, 1, 1], [3, 2, 1], [3, 2, 1]]) == False

def test_case_10():
    sol = Solution()
    assert sol.checkValid([[1, 2, 3], [1, 2, 3], [1, 1, 1]]) == False

