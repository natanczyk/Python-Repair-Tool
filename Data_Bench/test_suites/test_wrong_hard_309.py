# Test suite for wrong_hard_309  (slug: count-the-repetitions)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_309.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.getMaxRepetitions('acb', 4, 'ab', 2) == 2

def test_case_2():
    sol = Solution()
    assert sol.getMaxRepetitions('acb', 1, 'acb', 1) == 1

def test_case_3():
    sol = Solution()
    assert sol.getMaxRepetitions('', 4, 'ab', 2) == 0

def test_case_4():
    sol = Solution()
    assert sol.getMaxRepetitions('a', 4, 'ab', 2) == 0

def test_case_5():
    sol = Solution()
    assert sol.getMaxRepetitions('z', 4, 'ab', 2) == 0

def test_case_6():
    sol = Solution()
    assert sol.getMaxRepetitions('bca', 4, 'ab', 2) == 1

def test_case_7():
    sol = Solution()
    assert sol.getMaxRepetitions('acba', 4, 'ab', 2) == 2

def test_case_8():
    sol = Solution()
    assert sol.getMaxRepetitions('aaa', 4, 'ab', 2) == 0

def test_case_9():
    sol = Solution()
    assert sol.getMaxRepetitions('acb', 0, 'ab', 2) == 0

def test_case_10():
    sol = Solution()
    assert sol.getMaxRepetitions('acb', 1, 'ab', 2) == 0

def test_case_11():
    sol = Solution()
    assert sol.getMaxRepetitions('acb', 3, 'ab', 2) == 1

def test_case_12():
    sol = Solution()
    assert sol.getMaxRepetitions('acb', 4, 'ab', 2) == 2

def test_case_13():
    sol = Solution()
    assert sol.getMaxRepetitions('acb', 5, 'ab', 2) == 2

def test_case_14():
    sol = Solution()
    assert sol.getMaxRepetitions('acb', 8, 'ab', 2) == 4

def test_case_15():
    sol = Solution()
    assert sol.getMaxRepetitions('acb', 14, 'ab', 2) == 7

