# Test suite for wrong_easy_087  (slug: verifying-an-alien-dictionary)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_087.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.isAlienSorted(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz') == True

def test_case_2():
    sol = Solution()
    assert sol.isAlienSorted(['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz') == False

def test_case_3():
    sol = Solution()
    assert sol.isAlienSorted(['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz') == False

def test_case_4():
    sol = Solution()
    assert sol.isAlienSorted([], 'hlabcdefgijkmnopqrstuvwxyz') == True

def test_case_5():
    sol = Solution()
    assert sol.isAlienSorted(['hello'], 'hlabcdefgijkmnopqrstuvwxyz') == True

def test_case_6():
    sol = Solution()
    assert sol.isAlienSorted(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz') == True

def test_case_7():
    sol = Solution()
    assert sol.isAlienSorted(['leetcode', 'hello'], 'hlabcdefgijkmnopqrstuvwxyz') == False

def test_case_8():
    sol = Solution()
    assert sol.isAlienSorted(['hello', 'leetcode', 'x'], 'hlabcdefgijkmnopqrstuvwxyz') == True

def test_case_9():
    sol = Solution()
    assert sol.isAlienSorted(['hello', 'leetcode'], '') == True

def test_case_10():
    sol = Solution()
    assert sol.isAlienSorted(['hello', 'leetcode'], 'a') == True

def test_case_11():
    sol = Solution()
    assert sol.isAlienSorted(['hello', 'leetcode'], 'z') == True

def test_case_12():
    sol = Solution()
    assert sol.isAlienSorted(['hello', 'leetcode'], 'zyxwvutsrqponmkjigfedcbalh') == False

def test_case_13():
    sol = Solution()
    assert sol.isAlienSorted(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyza') == True

def test_case_14():
    sol = Solution()
    assert sol.isAlienSorted(['hello', 'leetcode'], 'aaaaaaaaaaaaaaaaaaaaaaaaaa') == True

def test_case_15():
    sol = Solution()
    assert sol.isAlienSorted([], 'worldabcefghijkmnpqstuvxyz') == True

