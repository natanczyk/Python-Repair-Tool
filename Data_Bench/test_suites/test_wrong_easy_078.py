# Test suite for wrong_easy_078  (slug: rings-and-rods)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_078.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.countPoints('B0B6G0R6R0R6G9') == 1

def test_case_2():
    sol = Solution()
    assert sol.countPoints('B0R0G0R9R0B0G0') == 1

def test_case_3():
    sol = Solution()
    assert sol.countPoints('G4') == 0

def test_case_4():
    sol = Solution()
    assert sol.countPoints('') == 0

def test_case_5():
    sol = Solution()
    assert sol.countPoints('a') == 0

def test_case_6():
    sol = Solution()
    assert sol.countPoints('z') == 0

def test_case_7():
    sol = Solution()
    assert sol.countPoints('9G6R0R6R0G6B0B') == 0

def test_case_8():
    sol = Solution()
    assert sol.countPoints('B0B6G0R6R0R6G9a') == 1

def test_case_9():
    sol = Solution()
    assert sol.countPoints('aaaaaaaaaaaaaa') == 0

def test_case_10():
    sol = Solution()
    assert sol.countPoints('') == 0

def test_case_11():
    sol = Solution()
    assert sol.countPoints('a') == 0

def test_case_12():
    sol = Solution()
    assert sol.countPoints('z') == 0

def test_case_13():
    sol = Solution()
    assert sol.countPoints('0G0B0R9R0G0R0B') == 0

def test_case_14():
    sol = Solution()
    assert sol.countPoints('B0R0G0R9R0B0G0a') == 1

def test_case_15():
    sol = Solution()
    assert sol.countPoints('aaaaaaaaaaaaaa') == 0

