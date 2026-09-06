# Test suite for wrong_easy_089  (slug: check-if-one-string-swap-can-make-strings-equal)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_089.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.areAlmostEqual('bank', 'kanb') == True

def test_case_2():
    sol = Solution()
    assert sol.areAlmostEqual('attack', 'defend') == False

def test_case_3():
    sol = Solution()
    assert sol.areAlmostEqual('kelb', 'kelb') == True

def test_case_4():
    sol = Solution()
    assert sol.areAlmostEqual('', 'kanb') == False

def test_case_5():
    sol = Solution()
    assert sol.areAlmostEqual('a', 'kanb') == False

def test_case_6():
    sol = Solution()
    assert sol.areAlmostEqual('z', 'kanb') == False

def test_case_7():
    sol = Solution()
    assert sol.areAlmostEqual('knab', 'kanb') == True

def test_case_8():
    sol = Solution()
    assert sol.areAlmostEqual('banka', 'kanb') == False

def test_case_9():
    sol = Solution()
    assert sol.areAlmostEqual('aaaa', 'kanb') == False

def test_case_10():
    sol = Solution()
    assert sol.areAlmostEqual('bank', '') == False

def test_case_11():
    sol = Solution()
    assert sol.areAlmostEqual('bank', 'a') == False

def test_case_12():
    sol = Solution()
    assert sol.areAlmostEqual('bank', 'z') == False

def test_case_13():
    sol = Solution()
    assert sol.areAlmostEqual('bank', 'bnak') == True

def test_case_14():
    sol = Solution()
    assert sol.areAlmostEqual('bank', 'kanba') == False

def test_case_15():
    sol = Solution()
    assert sol.areAlmostEqual('bank', 'aaaa') == False

