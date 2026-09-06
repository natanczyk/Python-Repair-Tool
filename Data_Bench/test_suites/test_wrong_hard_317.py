# Test suite for wrong_hard_317  (slug: check-if-string-is-transformable-with-substring-sort-operations)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_317.py'
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
    assert sol.isTransformable('a', '34852') == False

def test_case_6():
    sol = Solution()
    assert sol.isTransformable('z', '34852') == False

def test_case_7():
    sol = Solution()
    assert sol.isTransformable('23548', '34852') == False

def test_case_8():
    sol = Solution()
    assert sol.isTransformable('84532a', '34852') == False

def test_case_9():
    sol = Solution()
    assert sol.isTransformable('aaaaa', '34852') == False

def test_case_10():
    sol = Solution()
    assert sol.isTransformable('84532', '') == False

def test_case_11():
    sol = Solution()
    assert sol.isTransformable('84532', 'a') == False

def test_case_12():
    sol = Solution()
    assert sol.isTransformable('84532', 'z') == False

def test_case_13():
    sol = Solution()
    assert sol.isTransformable('84532', '25843') == False

def test_case_14():
    sol = Solution()
    assert sol.isTransformable('84532', '34852a') == False

def test_case_15():
    sol = Solution()
    assert sol.isTransformable('84532', 'aaaaa') == False

