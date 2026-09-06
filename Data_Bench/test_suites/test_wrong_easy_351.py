# Test suite for wrong_easy_351  (slug: largest-number-after-digit-swaps-by-parity)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_351.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.largestInteger(1234) == 3412

def test_case_2():
    sol = Solution()
    assert sol.largestInteger(65875) == 87655

def test_case_3():
    sol = Solution()
    assert sol.largestInteger(0) == 0

def test_case_4():
    sol = Solution()
    assert sol.largestInteger(1) == 1

def test_case_5():
    sol = Solution()
    assert sol.largestInteger(2468) == 8642

def test_case_6():
    sol = Solution()
    assert sol.largestInteger(1233) == 3231

def test_case_7():
    sol = Solution()
    assert sol.largestInteger(1234) == 3412

def test_case_8():
    sol = Solution()
    assert sol.largestInteger(1235) == 5231

def test_case_9():
    sol = Solution()
    assert sol.largestInteger(1244) == 1442

def test_case_10():
    sol = Solution()
    assert sol.largestInteger(0) == 0

def test_case_11():
    sol = Solution()
    assert sol.largestInteger(1) == 1

def test_case_12():
    sol = Solution()
    assert sol.largestInteger(131750) == 753110

def test_case_13():
    sol = Solution()
    assert sol.largestInteger(65874) == 87654

def test_case_14():
    sol = Solution()
    assert sol.largestInteger(65875) == 87655

def test_case_15():
    sol = Solution()
    assert sol.largestInteger(65876) == 87656

