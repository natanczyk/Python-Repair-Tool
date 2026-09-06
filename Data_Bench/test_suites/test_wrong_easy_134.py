# Test suite for wrong_easy_134  (slug: check-whether-two-strings-are-almost-equivalent)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_134.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.checkAlmostEquivalent('aaaa', 'bccb') == False

def test_case_2():
    sol = Solution()
    assert sol.checkAlmostEquivalent('abcdeef', 'abaaacc') == True

def test_case_3():
    sol = Solution()
    assert sol.checkAlmostEquivalent('cccddabba', 'babababab') == True

def test_case_4():
    sol = Solution()
    assert sol.checkAlmostEquivalent('', 'bccb') == True

def test_case_5():
    sol = Solution()
    assert sol.checkAlmostEquivalent('a', 'bccb') == True

def test_case_6():
    sol = Solution()
    assert sol.checkAlmostEquivalent('z', 'bccb') == True

def test_case_7():
    sol = Solution()
    assert sol.checkAlmostEquivalent('aaaa', 'bccb') == False

def test_case_8():
    sol = Solution()
    assert sol.checkAlmostEquivalent('aaaaa', 'bccb') == False

def test_case_9():
    sol = Solution()
    assert sol.checkAlmostEquivalent('aaaa', '') == False

def test_case_10():
    sol = Solution()
    assert sol.checkAlmostEquivalent('aaaa', 'a') == True

def test_case_11():
    sol = Solution()
    assert sol.checkAlmostEquivalent('aaaa', 'z') == False

def test_case_12():
    sol = Solution()
    assert sol.checkAlmostEquivalent('aaaa', 'bccb') == False

def test_case_13():
    sol = Solution()
    assert sol.checkAlmostEquivalent('aaaa', 'bccba') == True

def test_case_14():
    sol = Solution()
    assert sol.checkAlmostEquivalent('aaaa', 'aaaa') == True

def test_case_15():
    sol = Solution()
    assert sol.checkAlmostEquivalent('', 'abaaacc') == False

