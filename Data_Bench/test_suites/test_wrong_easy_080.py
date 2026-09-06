# Test suite for wrong_easy_080  (slug: ransom-note)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_080.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.canConstruct('a', 'b') == False

def test_case_2():
    sol = Solution()
    assert sol.canConstruct('aa', 'ab') == False

def test_case_3():
    sol = Solution()
    assert sol.canConstruct('aa', 'aab') == True

def test_case_4():
    sol = Solution()
    assert sol.canConstruct('', 'b') == True

def test_case_5():
    sol = Solution()
    assert sol.canConstruct('a', 'b') == False

def test_case_6():
    sol = Solution()
    assert sol.canConstruct('z', 'b') == False

def test_case_7():
    sol = Solution()
    assert sol.canConstruct('aa', 'b') == False

def test_case_8():
    sol = Solution()
    assert sol.canConstruct('a', '') == False

def test_case_9():
    sol = Solution()
    assert sol.canConstruct('a', 'a') == True

def test_case_10():
    sol = Solution()
    assert sol.canConstruct('a', 'z') == False

def test_case_11():
    sol = Solution()
    assert sol.canConstruct('a', 'b') == False

def test_case_12():
    sol = Solution()
    assert sol.canConstruct('a', 'ba') == True

def test_case_13():
    sol = Solution()
    assert sol.canConstruct('', 'ab') == True

def test_case_14():
    sol = Solution()
    assert sol.canConstruct('a', 'ab') == True

def test_case_15():
    sol = Solution()
    assert sol.canConstruct('z', 'ab') == False

