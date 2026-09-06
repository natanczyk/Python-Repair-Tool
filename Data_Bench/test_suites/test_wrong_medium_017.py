# Test suite for wrong_medium_017  (slug: lexicographical-numbers)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_017.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.lexicalOrder(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

def test_case_2():
    sol = Solution()
    assert sol.lexicalOrder(2) == [1, 2]

def test_case_3():
    sol = Solution()
    assert sol.lexicalOrder(0) == []

def test_case_4():
    sol = Solution()
    assert sol.lexicalOrder(1) == [1]

def test_case_5():
    sol = Solution()
    assert sol.lexicalOrder(12) == [1, 10, 11, 12, 2, 3, 4, 5, 6, 7, 8, 9]

def test_case_6():
    sol = Solution()
    assert sol.lexicalOrder(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

def test_case_7():
    sol = Solution()
    assert sol.lexicalOrder(14) == [1, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9]

def test_case_8():
    sol = Solution()
    assert sol.lexicalOrder(23) == [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 3, 4, 5, 6, 7, 8, 9]

def test_case_9():
    sol = Solution()
    assert sol.lexicalOrder(26) == [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 3, 4, 5, 6, 7, 8, 9]

def test_case_10():
    sol = Solution()
    assert sol.lexicalOrder(-1) == []

def test_case_11():
    sol = Solution()
    assert sol.lexicalOrder(0) == []

def test_case_12():
    sol = Solution()
    assert sol.lexicalOrder(1) == [1]

def test_case_13():
    sol = Solution()
    assert sol.lexicalOrder(2) == [1, 2]

def test_case_14():
    sol = Solution()
    assert sol.lexicalOrder(3) == [1, 2, 3]

def test_case_15():
    sol = Solution()
    assert sol.lexicalOrder(4) == [1, 2, 3, 4]

