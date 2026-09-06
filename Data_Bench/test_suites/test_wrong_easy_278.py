# Test suite for wrong_easy_278  (slug: increasing-decreasing-string)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_278.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.sortString('aaaabbbbcccc') == 'abccbaabccba'

def test_case_2():
    sol = Solution()
    assert sol.sortString('rat') == 'art'

def test_case_3():
    sol = Solution()
    assert sol.sortString('') == ''

def test_case_4():
    sol = Solution()
    assert sol.sortString('a') == 'a'

def test_case_5():
    sol = Solution()
    assert sol.sortString('z') == 'z'

def test_case_6():
    sol = Solution()
    assert sol.sortString('ccccbbbbaaaa') == 'abccbaabccba'

def test_case_7():
    sol = Solution()
    assert sol.sortString('aaaabbbbcccca') == 'abccbaabccbaa'

def test_case_8():
    sol = Solution()
    assert sol.sortString('aaaaaaaaaaaa') == 'aaaaaaaaaaaa'

def test_case_9():
    sol = Solution()
    assert sol.sortString('') == ''

def test_case_10():
    sol = Solution()
    assert sol.sortString('a') == 'a'

def test_case_11():
    sol = Solution()
    assert sol.sortString('z') == 'z'

def test_case_12():
    sol = Solution()
    assert sol.sortString('tar') == 'art'

def test_case_13():
    sol = Solution()
    assert sol.sortString('rata') == 'arta'

def test_case_14():
    sol = Solution()
    assert sol.sortString('aaa') == 'aaa'

