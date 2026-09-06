# Test suite for wrong_hard_028  (slug: longest-happy-prefix)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_028.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.longestPrefix('a') == ''

def test_case_2():
    sol = Solution()
    assert sol.longestPrefix('z') == ''

def test_case_3():
    sol = Solution()
    assert sol.longestPrefix('level') == 'l'

def test_case_4():
    sol = Solution()
    assert sol.longestPrefix('levela') == ''

def test_case_5():
    sol = Solution()
    assert sol.longestPrefix('aaaaa') == 'aaaa'

def test_case_6():
    sol = Solution()
    assert sol.longestPrefix('a') == ''

def test_case_7():
    sol = Solution()
    assert sol.longestPrefix('z') == ''

def test_case_8():
    sol = Solution()
    assert sol.longestPrefix('bababa') == 'baba'

def test_case_9():
    sol = Solution()
    assert sol.longestPrefix('abababa') == 'ababa'

def test_case_10():
    sol = Solution()
    assert sol.longestPrefix('aaaaaa') == 'aaaaa'

