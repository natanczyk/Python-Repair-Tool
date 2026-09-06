# Test suite for wrong_easy_129  (slug: check-if-two-string-arrays-are-equivalent)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_129.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['ab', 'c'], ['a', 'bc']) == True

def test_case_2():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['a', 'cb'], ['ab', 'c']) == False

def test_case_3():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['abc', 'd', 'defg'], ['abcddefg']) == True

def test_case_4():
    sol = Solution()
    assert sol.arrayStringsAreEqual([], ['a', 'bc']) == False

def test_case_5():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['ab'], ['a', 'bc']) == False

def test_case_6():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['ab', 'c'], ['a', 'bc']) == True

def test_case_7():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['c', 'ab'], ['a', 'bc']) == False

def test_case_8():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['ab', 'c', 'x'], ['a', 'bc']) == False

def test_case_9():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['ab', 'c'], []) == False

def test_case_10():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['ab', 'c'], ['a']) == False

def test_case_11():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['ab', 'c'], ['a', 'bc']) == True

def test_case_12():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['ab', 'c'], ['bc', 'a']) == False

def test_case_13():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['ab', 'c'], ['a', 'bc', 'x']) == False

def test_case_14():
    sol = Solution()
    assert sol.arrayStringsAreEqual([], ['ab', 'c']) == False

def test_case_15():
    sol = Solution()
    assert sol.arrayStringsAreEqual(['a'], ['ab', 'c']) == False

