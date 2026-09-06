# Test suite for wrong_easy_024  (slug: find-first-palindromic-string-in-the-array)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_024.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.firstPalindrome(['abc', 'car', 'ada', 'racecar', 'cool']) == 'ada'

def test_case_2():
    sol = Solution()
    assert sol.firstPalindrome(['notapalindrome', 'racecar']) == 'racecar'

def test_case_3():
    sol = Solution()
    assert sol.firstPalindrome(['def', 'ghi']) == ''

def test_case_4():
    sol = Solution()
    assert sol.firstPalindrome([]) == ''

def test_case_5():
    sol = Solution()
    assert sol.firstPalindrome(['abc']) == ''

def test_case_6():
    sol = Solution()
    assert sol.firstPalindrome(['abc', 'ada', 'car', 'cool', 'racecar']) == 'ada'

def test_case_7():
    sol = Solution()
    assert sol.firstPalindrome(['cool', 'racecar', 'ada', 'car', 'abc']) == 'racecar'

def test_case_8():
    sol = Solution()
    assert sol.firstPalindrome(['abc', 'car', 'ada', 'racecar', 'cool', 'x']) == 'ada'

def test_case_9():
    sol = Solution()
    assert sol.firstPalindrome([]) == ''

def test_case_10():
    sol = Solution()
    assert sol.firstPalindrome(['notapalindrome']) == ''

def test_case_11():
    sol = Solution()
    assert sol.firstPalindrome(['notapalindrome', 'racecar']) == 'racecar'

def test_case_12():
    sol = Solution()
    assert sol.firstPalindrome(['racecar', 'notapalindrome']) == 'racecar'

def test_case_13():
    sol = Solution()
    assert sol.firstPalindrome(['notapalindrome', 'racecar', 'x']) == 'racecar'

def test_case_14():
    sol = Solution()
    assert sol.firstPalindrome([]) == ''

def test_case_15():
    sol = Solution()
    assert sol.firstPalindrome(['def']) == ''

