# Test suite for wrong_hard_414  (slug: check-if-string-is-transformable-with-substring-sort-operations)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_414.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.isTransformable('84532', '34852') == True

def test_case_2():
    sol = Solution()
    assert sol.isTransformable('34521', '23415') == True

def test_case_3():
    sol = Solution()
    assert sol.isTransformable('12345', '12435') == False

def test_case_4():
    sol = Solution()
    assert sol.isTransformable('', '34852') == False

def test_case_5():
    sol = Solution()
    assert sol.isTransformable('23548', '34852') == False

def test_case_6():
    sol = Solution()
    assert sol.isTransformable('84532', '') == True

def test_case_7():
    sol = Solution()
    assert sol.isTransformable('84532', '25843') == False

def test_case_8():
    sol = Solution()
    assert sol.isTransformable('', '23415') == False

def test_case_9():
    sol = Solution()
    assert sol.isTransformable('12543', '23415') == False

def test_case_10():
    sol = Solution()
    assert sol.isTransformable('34521', '') == True

def test_case_11():
    sol = Solution()
    assert sol.isTransformable('34521', '51432') == False

def test_case_12():
    sol = Solution()
    assert sol.isTransformable('', '12435') == False

def test_case_13():
    sol = Solution()
    assert sol.isTransformable('54321', '12435') == True

def test_case_14():
    sol = Solution()
    assert sol.isTransformable('12345', '') == True

def test_case_15():
    sol = Solution()
    assert sol.isTransformable('12345', '53421') == False

