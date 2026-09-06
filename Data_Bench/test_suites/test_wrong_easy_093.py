# Test suite for wrong_easy_093  (slug: most-common-word)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_093.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']) == 'ball'

def test_case_2():
    sol = Solution()
    assert sol.mostCommonWord('a.', []) == 'a'

def test_case_3():
    sol = Solution()
    assert sol.mostCommonWord('a', ['hit']) == 'a'

def test_case_4():
    sol = Solution()
    assert sol.mostCommonWord('z', ['hit']) == 'z'

def test_case_5():
    sol = Solution()
    assert sol.mostCommonWord('.tih saw ti retfa raf welf LLAB tih eht ,llab a tih boB', ['hit']) == 'tih'

def test_case_6():
    sol = Solution()
    assert sol.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.a', ['hit']) == 'a'

def test_case_7():
    sol = Solution()
    assert sol.mostCommonWord('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ['hit']) == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

def test_case_8():
    sol = Solution()
    assert sol.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', []) == 'hit'

def test_case_9():
    sol = Solution()
    assert sol.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']) == 'ball'

def test_case_10():
    sol = Solution()
    assert sol.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']) == 'ball'

def test_case_11():
    sol = Solution()
    assert sol.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']) == 'ball'

def test_case_12():
    sol = Solution()
    assert sol.mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit', 'x']) == 'ball'

def test_case_13():
    sol = Solution()
    assert sol.mostCommonWord('a', []) == 'a'

def test_case_14():
    sol = Solution()
    assert sol.mostCommonWord('z', []) == 'z'

def test_case_15():
    sol = Solution()
    assert sol.mostCommonWord('.a', []) == 'a'

