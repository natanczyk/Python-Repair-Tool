# Test suite for wrong_hard_410  (slug: count-anagrams)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_410.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.countAnagrams('too hot') == 18

def test_case_2():
    sol = Solution()
    assert sol.countAnagrams('aa') == 1

def test_case_3():
    sol = Solution()
    assert sol.countAnagrams('') == 1

def test_case_4():
    sol = Solution()
    assert sol.countAnagrams('a') == 1

def test_case_5():
    sol = Solution()
    assert sol.countAnagrams('z') == 1

def test_case_6():
    sol = Solution()
    assert sol.countAnagrams('toh oot') == 18

def test_case_7():
    sol = Solution()
    assert sol.countAnagrams('too hota') == 72

def test_case_8():
    sol = Solution()
    assert sol.countAnagrams('aaaaaaa') == 1

def test_case_9():
    sol = Solution()
    assert sol.countAnagrams('') == 1

def test_case_10():
    sol = Solution()
    assert sol.countAnagrams('a') == 1

def test_case_11():
    sol = Solution()
    assert sol.countAnagrams('z') == 1

def test_case_12():
    sol = Solution()
    assert sol.countAnagrams('aa') == 1

def test_case_13():
    sol = Solution()
    assert sol.countAnagrams('aaa') == 1

