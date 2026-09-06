# Test suite for wrong_easy_308  (slug: find-words-that-can-be-formed-by-characters)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_308.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.countCharacters(['cat', 'bt', 'hat', 'tree'], 'atach') == 6

def test_case_2():
    sol = Solution()
    assert sol.countCharacters(['hello', 'world', 'leetcode'], 'welldonehoneyr') == 10

def test_case_3():
    sol = Solution()
    assert sol.countCharacters([], 'atach') == 0

def test_case_4():
    sol = Solution()
    assert sol.countCharacters(['cat'], 'atach') == 3

def test_case_5():
    sol = Solution()
    assert sol.countCharacters(['bt', 'cat', 'hat', 'tree'], 'atach') == 6

def test_case_6():
    sol = Solution()
    assert sol.countCharacters(['tree', 'hat', 'bt', 'cat'], 'atach') == 6

def test_case_7():
    sol = Solution()
    assert sol.countCharacters(['cat', 'bt', 'hat', 'tree', 'x'], 'atach') == 6

def test_case_8():
    sol = Solution()
    assert sol.countCharacters(['cat', 'bt', 'hat', 'tree'], '') == 0

def test_case_9():
    sol = Solution()
    assert sol.countCharacters(['cat', 'bt', 'hat', 'tree'], 'a') == 0

def test_case_10():
    sol = Solution()
    assert sol.countCharacters(['cat', 'bt', 'hat', 'tree'], 'z') == 0

def test_case_11():
    sol = Solution()
    assert sol.countCharacters(['cat', 'bt', 'hat', 'tree'], 'hcata') == 6

def test_case_12():
    sol = Solution()
    assert sol.countCharacters(['cat', 'bt', 'hat', 'tree'], 'atacha') == 6

def test_case_13():
    sol = Solution()
    assert sol.countCharacters(['cat', 'bt', 'hat', 'tree'], 'aaaaa') == 0

def test_case_14():
    sol = Solution()
    assert sol.countCharacters([], 'welldonehoneyr') == 0

def test_case_15():
    sol = Solution()
    assert sol.countCharacters(['hello'], 'welldonehoneyr') == 5

