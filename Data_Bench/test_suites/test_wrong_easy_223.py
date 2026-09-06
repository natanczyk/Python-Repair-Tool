# Test suite for wrong_easy_223  (slug: lexicographically-smallest-palindrome)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_223.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.makeSmallestPalindrome('egcfe') == 'efcfe'

def test_case_2():
    sol = Solution()
    assert sol.makeSmallestPalindrome('abcd') == 'abba'

def test_case_3():
    sol = Solution()
    assert sol.makeSmallestPalindrome('seven') == 'neven'

def test_case_4():
    sol = Solution()
    assert sol.makeSmallestPalindrome('a') == 'a'

def test_case_5():
    sol = Solution()
    assert sol.makeSmallestPalindrome('z') == 'z'

def test_case_6():
    sol = Solution()
    assert sol.makeSmallestPalindrome('efcge') == 'efcfe'

def test_case_7():
    sol = Solution()
    assert sol.makeSmallestPalindrome('egcfea') == 'aeccea'

def test_case_8():
    sol = Solution()
    assert sol.makeSmallestPalindrome('aaaaa') == 'aaaaa'

def test_case_9():
    sol = Solution()
    assert sol.makeSmallestPalindrome('a') == 'a'

def test_case_10():
    sol = Solution()
    assert sol.makeSmallestPalindrome('z') == 'z'

def test_case_11():
    sol = Solution()
    assert sol.makeSmallestPalindrome('dcba') == 'abba'

def test_case_12():
    sol = Solution()
    assert sol.makeSmallestPalindrome('abcda') == 'abcba'

def test_case_13():
    sol = Solution()
    assert sol.makeSmallestPalindrome('aaaa') == 'aaaa'

def test_case_14():
    sol = Solution()
    assert sol.makeSmallestPalindrome('a') == 'a'

def test_case_15():
    sol = Solution()
    assert sol.makeSmallestPalindrome('z') == 'z'

