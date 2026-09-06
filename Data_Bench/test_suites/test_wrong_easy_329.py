# Test suite for wrong_easy_329  (slug: substrings-of-size-three-with-distinct-characters)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_329.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.countGoodSubstrings('xyzzaz') == 1

def test_case_2():
    sol = Solution()
    assert sol.countGoodSubstrings('aababcabc') == 4

def test_case_3():
    sol = Solution()
    assert sol.countGoodSubstrings('') == 0

def test_case_4():
    sol = Solution()
    assert sol.countGoodSubstrings('a') == 0

def test_case_5():
    sol = Solution()
    assert sol.countGoodSubstrings('z') == 0

def test_case_6():
    sol = Solution()
    assert sol.countGoodSubstrings('zazzyx') == 1

def test_case_7():
    sol = Solution()
    assert sol.countGoodSubstrings('xyzzaza') == 1

def test_case_8():
    sol = Solution()
    assert sol.countGoodSubstrings('aaaaaa') == 0

def test_case_9():
    sol = Solution()
    assert sol.countGoodSubstrings('') == 0

def test_case_10():
    sol = Solution()
    assert sol.countGoodSubstrings('a') == 0

def test_case_11():
    sol = Solution()
    assert sol.countGoodSubstrings('z') == 0

def test_case_12():
    sol = Solution()
    assert sol.countGoodSubstrings('cbacbabaa') == 4

def test_case_13():
    sol = Solution()
    assert sol.countGoodSubstrings('aababcabca') == 5

def test_case_14():
    sol = Solution()
    assert sol.countGoodSubstrings('aaaaaaaaa') == 0

