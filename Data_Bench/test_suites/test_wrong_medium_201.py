# Test suite for wrong_medium_201  (slug: lexicographically-smallest-string-after-substring-operation)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_201.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.smallestString('') == 'z'

def test_case_2():
    sol = Solution()
    assert sol.smallestString('a') == 'z'

def test_case_3():
    sol = Solution()
    assert sol.smallestString('z') == 'y'

def test_case_4():
    sol = Solution()
    assert sol.smallestString('cbabc') == 'baabc'

def test_case_5():
    sol = Solution()
    assert sol.smallestString('cbabca') == 'baabca'

def test_case_6():
    sol = Solution()
    assert sol.smallestString('aaaaa') == 'aaaaz'

def test_case_7():
    sol = Solution()
    assert sol.smallestString('') == 'z'

def test_case_8():
    sol = Solution()
    assert sol.smallestString('a') == 'z'

def test_case_9():
    sol = Solution()
    assert sol.smallestString('z') == 'y'

def test_case_10():
    sol = Solution()
    assert sol.smallestString('cbbca') == 'baaba'

def test_case_11():
    sol = Solution()
    assert sol.smallestString('acbbca') == 'abaaba'

def test_case_12():
    sol = Solution()
    assert sol.smallestString('aaaaa') == 'aaaaz'

def test_case_13():
    sol = Solution()
    assert sol.smallestString('') == 'z'

def test_case_14():
    sol = Solution()
    assert sol.smallestString('a') == 'z'

def test_case_15():
    sol = Solution()
    assert sol.smallestString('z') == 'y'

