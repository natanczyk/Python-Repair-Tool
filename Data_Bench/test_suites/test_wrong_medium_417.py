# Test suite for wrong_medium_417  (slug: number-of-pairs-of-strings-with-concatenation-equal-to-target)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_417.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.numOfPairs(['777', '7', '77', '77'], '7777') == 4

def test_case_2():
    sol = Solution()
    assert sol.numOfPairs(['123', '4', '12', '34'], '1234') == 2

def test_case_3():
    sol = Solution()
    assert sol.numOfPairs(['1', '1', '1'], '11') == 6

def test_case_4():
    sol = Solution()
    assert sol.numOfPairs([], '7777') == 0

def test_case_5():
    sol = Solution()
    assert sol.numOfPairs(['777'], '7777') == 0

def test_case_6():
    sol = Solution()
    assert sol.numOfPairs(['7', '77', '77', '777'], '7777') == 4

def test_case_7():
    sol = Solution()
    assert sol.numOfPairs(['77', '77', '7', '777'], '7777') == 4

def test_case_8():
    sol = Solution()
    assert sol.numOfPairs(['777', '7', '77', '77', 'x'], '7777') == 4

def test_case_9():
    sol = Solution()
    assert sol.numOfPairs(['777', '7', '77', '77'], '') == 0

def test_case_10():
    sol = Solution()
    assert sol.numOfPairs(['777', '7', '77', '77'], 'a') == 0

def test_case_11():
    sol = Solution()
    assert sol.numOfPairs(['777', '7', '77', '77'], 'z') == 0

def test_case_12():
    sol = Solution()
    assert sol.numOfPairs(['777', '7', '77', '77'], '7777') == 4

def test_case_13():
    sol = Solution()
    assert sol.numOfPairs(['777', '7', '77', '77'], '7777a') == 0

def test_case_14():
    sol = Solution()
    assert sol.numOfPairs(['777', '7', '77', '77'], 'aaaa') == 0

def test_case_15():
    sol = Solution()
    assert sol.numOfPairs([], '1234') == 0

