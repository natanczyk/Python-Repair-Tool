# Test suite for wrong_hard_407  (slug: palindrome-partitioning-iii)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_407.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.palindromePartition('abc', 2) == 1

def test_case_2():
    sol = Solution()
    assert sol.palindromePartition('aabbc', 3) == 0

def test_case_3():
    sol = Solution()
    assert sol.palindromePartition('leetcode', 8) == 0

def test_case_4():
    sol = Solution()
    assert sol.palindromePartition('', 2) == inf

def test_case_5():
    sol = Solution()
    assert sol.palindromePartition('a', 2) == inf

def test_case_6():
    sol = Solution()
    assert sol.palindromePartition('z', 2) == inf

def test_case_7():
    sol = Solution()
    assert sol.palindromePartition('cba', 2) == 1

def test_case_8():
    sol = Solution()
    assert sol.palindromePartition('abca', 2) == 1

def test_case_9():
    sol = Solution()
    assert sol.palindromePartition('aaa', 2) == 0

def test_case_10():
    sol = Solution()
    assert sol.palindromePartition('abc', 0) == inf

def test_case_11():
    sol = Solution()
    assert sol.palindromePartition('abc', 1) == 1

def test_case_12():
    sol = Solution()
    assert sol.palindromePartition('abc', 2) == 1

def test_case_13():
    sol = Solution()
    assert sol.palindromePartition('abc', 3) == 0

def test_case_14():
    sol = Solution()
    assert sol.palindromePartition('abc', 4) == inf

def test_case_15():
    sol = Solution()
    assert sol.palindromePartition('abc', 12) == inf

