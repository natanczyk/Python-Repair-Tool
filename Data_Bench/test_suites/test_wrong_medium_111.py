# Test suite for wrong_medium_111  (slug: find-all-lonely-numbers-in-the-array)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_111.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.findLonely([10, 6, 5, 8]) == [10, 8]

def test_case_2():
    sol = Solution()
    assert sol.findLonely([1, 3, 5, 3]) == [1, 5]

def test_case_3():
    sol = Solution()
    assert sol.findLonely([]) == []

def test_case_4():
    sol = Solution()
    assert sol.findLonely([10]) == [10]

def test_case_5():
    sol = Solution()
    assert sol.findLonely([5, 6, 8, 10]) == [8, 10]

def test_case_6():
    sol = Solution()
    assert sol.findLonely([10, 8, 6, 5]) == [10, 8]

def test_case_7():
    sol = Solution()
    assert sol.findLonely([8, 5, 6, 10]) == [8, 10]

def test_case_8():
    sol = Solution()
    assert sol.findLonely([10, 6, 5, 8, 0]) == [10, 8, 0]

def test_case_9():
    sol = Solution()
    assert sol.findLonely([0, 0, 0, 0]) == []

def test_case_10():
    sol = Solution()
    assert sol.findLonely([1, 1, 1, 1]) == []

def test_case_11():
    sol = Solution()
    assert sol.findLonely([11, 7, 6, 9]) == [11, 9]

def test_case_12():
    sol = Solution()
    assert sol.findLonely([9, 5, 4, 7]) == [9, 7]

def test_case_13():
    sol = Solution()
    assert sol.findLonely([10, 6, 5, 8, 10, 6, 5, 8]) == []

def test_case_14():
    sol = Solution()
    assert sol.findLonely([8, 10, 5, 6]) == [8, 10]

def test_case_15():
    sol = Solution()
    assert sol.findLonely([]) == []

