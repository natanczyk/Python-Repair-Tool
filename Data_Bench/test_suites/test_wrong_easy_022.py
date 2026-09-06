# Test suite for wrong_easy_022  (slug: isomorphic-strings)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_022.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.isIsomorphic('egg', 'add') == True

def test_case_2():
    sol = Solution()
    assert sol.isIsomorphic('foo', 'bar') == False

def test_case_3():
    sol = Solution()
    assert sol.isIsomorphic('paper', 'title') == True

def test_case_4():
    sol = Solution()
    assert sol.isIsomorphic('', 'add') == False

def test_case_5():
    sol = Solution()
    assert sol.isIsomorphic('a', 'add') == False

def test_case_6():
    sol = Solution()
    assert sol.isIsomorphic('z', 'add') == False

def test_case_7():
    sol = Solution()
    assert sol.isIsomorphic('gge', 'add') == False

def test_case_8():
    sol = Solution()
    assert sol.isIsomorphic('egga', 'add') == False

def test_case_9():
    sol = Solution()
    assert sol.isIsomorphic('aaa', 'add') == False

def test_case_10():
    sol = Solution()
    assert sol.isIsomorphic('egg', '') == False

def test_case_11():
    sol = Solution()
    assert sol.isIsomorphic('egg', 'a') == False

def test_case_12():
    sol = Solution()
    assert sol.isIsomorphic('egg', 'z') == False

def test_case_13():
    sol = Solution()
    assert sol.isIsomorphic('egg', 'dda') == False

def test_case_14():
    sol = Solution()
    assert sol.isIsomorphic('egg', 'adda') == True

def test_case_15():
    sol = Solution()
    assert sol.isIsomorphic('egg', 'aaa') == False

