# Test suite for wrong_medium_555  (slug: plates-between-candles)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_555.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.platesBetweenCandles('**|**|***|', [[2, 5], [5, 9]]) == [2, 3]

def test_case_2():
    sol = Solution()
    assert sol.platesBetweenCandles('***|**|*****|**||**|*', [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) == [9, 0, 0, 0, 0]

def test_case_3():
    sol = Solution()
    assert sol.platesBetweenCandles('', [[2, 5], [5, 9]]) == [0, 0]

def test_case_4():
    sol = Solution()
    assert sol.platesBetweenCandles('a', [[2, 5], [5, 9]]) == [0, 0]

def test_case_5():
    sol = Solution()
    assert sol.platesBetweenCandles('z', [[2, 5], [5, 9]]) == [0, 0]

def test_case_6():
    sol = Solution()
    assert sol.platesBetweenCandles('|***|**|**', [[2, 5], [5, 9]]) == [0, 0]

def test_case_7():
    sol = Solution()
    assert sol.platesBetweenCandles('**|**|***|a', [[2, 5], [5, 9]]) == [2, 3]

def test_case_8():
    sol = Solution()
    assert sol.platesBetweenCandles('aaaaaaaaaa', [[2, 5], [5, 9]]) == [0, 0]

def test_case_9():
    sol = Solution()
    assert sol.platesBetweenCandles('**|**|***|', [[0, 0], [0, 0]]) == [0, 0]

def test_case_10():
    sol = Solution()
    assert sol.platesBetweenCandles('**|**|***|', [[1, 1], [1, 1]]) == [0, 0]

def test_case_11():
    sol = Solution()
    assert sol.platesBetweenCandles('**|**|***|', [[5, 2], [9, 5]]) == [0, 0]

def test_case_12():
    sol = Solution()
    assert sol.platesBetweenCandles('**|**|***|', [[5, 9], [2, 5]]) == [3, 2]

def test_case_13():
    sol = Solution()
    assert sol.platesBetweenCandles('', [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) == [0, 0, 0, 0, 0]

def test_case_14():
    sol = Solution()
    assert sol.platesBetweenCandles('a', [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) == [0, 0, 0, 0, 0]

def test_case_15():
    sol = Solution()
    assert sol.platesBetweenCandles('z', [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) == [0, 0, 0, 0, 0]

