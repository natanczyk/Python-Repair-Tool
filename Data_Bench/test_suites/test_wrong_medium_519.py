# Test suite for wrong_medium_519  (slug: delete-operation-for-two-strings)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_519.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.minDistance('', 'eat') == 3

def test_case_2():
    sol = Solution()
    assert sol.minDistance('a', 'eat') == 2

def test_case_3():
    sol = Solution()
    assert sol.minDistance('z', 'eat') == 4

def test_case_4():
    sol = Solution()
    assert sol.minDistance('aes', 'eat') == 4

def test_case_5():
    sol = Solution()
    assert sol.minDistance('seaa', 'eat') == 3

def test_case_6():
    sol = Solution()
    assert sol.minDistance('aaa', 'eat') == 4

def test_case_7():
    sol = Solution()
    assert sol.minDistance('sea', '') == 3

def test_case_8():
    sol = Solution()
    assert sol.minDistance('sea', 'a') == 2

def test_case_9():
    sol = Solution()
    assert sol.minDistance('sea', 'z') == 4

def test_case_10():
    sol = Solution()
    assert sol.minDistance('sea', 'tae') == 4

def test_case_11():
    sol = Solution()
    assert sol.minDistance('sea', 'eata') == 3

def test_case_12():
    sol = Solution()
    assert sol.minDistance('sea', 'aaa') == 4

def test_case_13():
    sol = Solution()
    assert sol.minDistance('', 'etco') == 4

def test_case_14():
    sol = Solution()
    assert sol.minDistance('a', 'etco') == 5

def test_case_15():
    sol = Solution()
    assert sol.minDistance('z', 'etco') == 5

