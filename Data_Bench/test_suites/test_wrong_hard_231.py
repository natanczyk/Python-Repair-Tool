# Test suite for wrong_hard_231  (slug: valid-permutations-for-di-sequence)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_231.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.numPermsDISequence('DID') == 5

def test_case_2():
    sol = Solution()
    assert sol.numPermsDISequence('D') == 1

def test_case_3():
    sol = Solution()
    assert sol.numPermsDISequence('') == 1

def test_case_4():
    sol = Solution()
    assert sol.numPermsDISequence('a') == 1

def test_case_5():
    sol = Solution()
    assert sol.numPermsDISequence('z') == 1

def test_case_6():
    sol = Solution()
    assert sol.numPermsDISequence('DID') == 5

def test_case_7():
    sol = Solution()
    assert sol.numPermsDISequence('DIDa') == 16

def test_case_8():
    sol = Solution()
    assert sol.numPermsDISequence('aaa') == 1

def test_case_9():
    sol = Solution()
    assert sol.numPermsDISequence('') == 1

def test_case_10():
    sol = Solution()
    assert sol.numPermsDISequence('a') == 1

def test_case_11():
    sol = Solution()
    assert sol.numPermsDISequence('z') == 1

def test_case_12():
    sol = Solution()
    assert sol.numPermsDISequence('D') == 1

def test_case_13():
    sol = Solution()
    assert sol.numPermsDISequence('Da') == 2

