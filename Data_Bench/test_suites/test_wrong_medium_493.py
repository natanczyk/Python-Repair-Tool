# Test suite for wrong_medium_493  (slug: number-of-ways-to-split-a-string)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_493.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.numWays('') == 1

def test_case_2():
    sol = Solution()
    assert sol.numWays('a') == 0

def test_case_3():
    sol = Solution()
    assert sol.numWays('z') == 0

def test_case_4():
    sol = Solution()
    assert sol.numWays('10101') == 4

def test_case_5():
    sol = Solution()
    assert sol.numWays('10101a') == 4

def test_case_6():
    sol = Solution()
    assert sol.numWays('aaaaa') == 6

def test_case_7():
    sol = Solution()
    assert sol.numWays('') == 1

def test_case_8():
    sol = Solution()
    assert sol.numWays('a') == 0

def test_case_9():
    sol = Solution()
    assert sol.numWays('z') == 0

def test_case_10():
    sol = Solution()
    assert sol.numWays('1001') == 0

def test_case_11():
    sol = Solution()
    assert sol.numWays('1001a') == 0

def test_case_12():
    sol = Solution()
    assert sol.numWays('aaaa') == 3

def test_case_13():
    sol = Solution()
    assert sol.numWays('') == 1

def test_case_14():
    sol = Solution()
    assert sol.numWays('a') == 0

def test_case_15():
    sol = Solution()
    assert sol.numWays('z') == 0

