# Test suite for wrong_medium_163  (slug: largest-number-after-mutating-substring)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_163.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.maximumNumber('132', [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == '832'

def test_case_2():
    sol = Solution()
    assert sol.maximumNumber('021', [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]) == '934'

def test_case_3():
    sol = Solution()
    assert sol.maximumNumber('5', [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]) == '5'

def test_case_4():
    sol = Solution()
    assert sol.maximumNumber('', [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == ''

def test_case_5():
    sol = Solution()
    assert sol.maximumNumber('231', [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == '531'

def test_case_6():
    sol = Solution()
    assert sol.maximumNumber('132a', [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == '832a'

def test_case_7():
    sol = Solution()
    assert sol.maximumNumber('132', [0, 2, 3, 4, 5, 6, 6, 8, 8, 9]) == '243'

def test_case_8():
    sol = Solution()
    assert sol.maximumNumber('132', [9, 8, 8, 6, 6, 5, 4, 3, 2, 0]) == '868'

def test_case_9():
    sol = Solution()
    assert sol.maximumNumber('132', [8, 6, 2, 4, 6, 3, 0, 5, 8, 9]) == '642'

def test_case_10():
    sol = Solution()
    assert sol.maximumNumber('132', [9, 8, 5, 0, 3, 6, 4, 2, 6, 8, 0]) == '832'

def test_case_11():
    sol = Solution()
    assert sol.maximumNumber('132', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == '132'

def test_case_12():
    sol = Solution()
    assert sol.maximumNumber('132', [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == '132'

def test_case_13():
    sol = Solution()
    assert sol.maximumNumber('132', [10, 9, 6, 1, 4, 7, 5, 3, 7, 9]) == '932'

def test_case_14():
    sol = Solution()
    assert sol.maximumNumber('132', [8, 7, 4, -1, 2, 5, 3, 1, 5, 7]) == '732'

def test_case_15():
    sol = Solution()
    assert sol.maximumNumber('132', [9, 8, 5, 0, 3, 6, 4, 2, 6, 8, 9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == '832'

