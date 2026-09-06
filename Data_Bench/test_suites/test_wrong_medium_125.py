# Test suite for wrong_medium_125  (slug: longest-substring-with-at-least-k-repeating-characters)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_125.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.longestSubstring('', 3) == 0

def test_case_2():
    sol = Solution()
    assert sol.longestSubstring('a', 3) == 0

def test_case_3():
    sol = Solution()
    assert sol.longestSubstring('z', 3) == 0

def test_case_4():
    sol = Solution()
    assert sol.longestSubstring('bbaaa', 3) == 3

def test_case_5():
    sol = Solution()
    assert sol.longestSubstring('aaabba', 3) == 3

def test_case_6():
    sol = Solution()
    assert sol.longestSubstring('aaaaa', 3) == 5

def test_case_7():
    sol = Solution()
    assert sol.longestSubstring('aaabb', 0) == 5

def test_case_8():
    sol = Solution()
    assert sol.longestSubstring('aaabb', 1) == 5

def test_case_9():
    sol = Solution()
    assert sol.longestSubstring('aaabb', 2) == 5

def test_case_10():
    sol = Solution()
    assert sol.longestSubstring('aaabb', 3) == 3

def test_case_11():
    sol = Solution()
    assert sol.longestSubstring('aaabb', 4) == 0

def test_case_12():
    sol = Solution()
    assert sol.longestSubstring('aaabb', 6) == 0

def test_case_13():
    sol = Solution()
    assert sol.longestSubstring('aaabb', 13) == 0

def test_case_14():
    sol = Solution()
    assert sol.longestSubstring('aaabb', -1) == 5

def test_case_15():
    sol = Solution()
    assert sol.longestSubstring('', 2) == 0

