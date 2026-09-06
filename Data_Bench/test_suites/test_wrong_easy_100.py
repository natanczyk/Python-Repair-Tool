# Test suite for wrong_easy_100  (slug: find-the-array-concatenation-value)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_100.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.findTheArrayConcVal([7, 52, 2, 4]) == 596

def test_case_2():
    sol = Solution()
    assert sol.findTheArrayConcVal([5, 14, 13, 8, 12]) == 673

def test_case_3():
    sol = Solution()
    assert sol.findTheArrayConcVal([]) == 0

def test_case_4():
    sol = Solution()
    assert sol.findTheArrayConcVal([7]) == 7

def test_case_5():
    sol = Solution()
    assert sol.findTheArrayConcVal([2, 4, 7, 52]) == 299

def test_case_6():
    sol = Solution()
    assert sol.findTheArrayConcVal([52, 7, 4, 2]) == 596

def test_case_7():
    sol = Solution()
    assert sol.findTheArrayConcVal([4, 2, 52, 7]) == 299

def test_case_8():
    sol = Solution()
    assert sol.findTheArrayConcVal([7, 52, 2, 4, 0]) == 596

def test_case_9():
    sol = Solution()
    assert sol.findTheArrayConcVal([0, 0, 0, 0]) == 0

def test_case_10():
    sol = Solution()
    assert sol.findTheArrayConcVal([1, 1, 1, 1]) == 22

def test_case_11():
    sol = Solution()
    assert sol.findTheArrayConcVal([8, 53, 3, 5]) == 618

def test_case_12():
    sol = Solution()
    assert sol.findTheArrayConcVal([6, 51, 1, 3]) == 574

def test_case_13():
    sol = Solution()
    assert sol.findTheArrayConcVal([7, 52, 2, 4, 7, 52, 2, 4]) == 895

def test_case_14():
    sol = Solution()
    assert sol.findTheArrayConcVal([2, 52, 4, 7]) == 551

def test_case_15():
    sol = Solution()
    assert sol.findTheArrayConcVal([]) == 0

