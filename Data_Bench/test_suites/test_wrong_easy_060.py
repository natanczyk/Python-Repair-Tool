# Test suite for wrong_easy_060  (slug: partition-array-into-three-parts-with-equal-sum)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_060.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) == True

def test_case_2():
    sol = Solution()
    assert sol.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) == False

def test_case_3():
    sol = Solution()
    assert sol.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]) == True

def test_case_4():
    sol = Solution()
    assert sol.canThreePartsEqualSum([]) == False

def test_case_5():
    sol = Solution()
    assert sol.canThreePartsEqualSum([0]) == False

def test_case_6():
    sol = Solution()
    assert sol.canThreePartsEqualSum([-7, -6, 0, 0, 1, 1, 1, 2, 2, 6, 9]) == False

def test_case_7():
    sol = Solution()
    assert sol.canThreePartsEqualSum([9, 6, 2, 2, 1, 1, 1, 0, 0, -6, -7]) == False

def test_case_8():
    sol = Solution()
    assert sol.canThreePartsEqualSum([1, 0, 2, 1, 9, -7, 6, -6, 1, 2, 0]) == True

def test_case_9():
    sol = Solution()
    assert sol.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1, 0]) == True

def test_case_10():
    sol = Solution()
    assert sol.canThreePartsEqualSum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True

def test_case_11():
    sol = Solution()
    assert sol.canThreePartsEqualSum([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False

def test_case_12():
    sol = Solution()
    assert sol.canThreePartsEqualSum([1, 3, 2, -5, 7, -6, 10, 2, 3, 1, 2]) == False

def test_case_13():
    sol = Solution()
    assert sol.canThreePartsEqualSum([-1, 1, 0, -7, 5, -8, 8, 0, 1, -1, 0]) == False

def test_case_14():
    sol = Solution()
    assert sol.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1, 0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) == True

def test_case_15():
    sol = Solution()
    assert sol.canThreePartsEqualSum([0, 1, 2, 6, 9, -7, -6]) == False

