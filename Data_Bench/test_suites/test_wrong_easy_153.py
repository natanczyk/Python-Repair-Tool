# Test suite for wrong_easy_153  (slug: capitalize-the-title)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_easy' / 'code' / 'wrong' / 'wrong_easy_153.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.capitalizeTitle('capiTalIze tHe titLe') == 'Capitalize The Title'

def test_case_2():
    sol = Solution()
    assert sol.capitalizeTitle('First leTTeR of EACH Word') == 'First Letter of Each Word'

def test_case_3():
    sol = Solution()
    assert sol.capitalizeTitle('i lOve leetcode') == 'i Love Leetcode'

def test_case_4():
    sol = Solution()
    assert sol.capitalizeTitle('') == ''

def test_case_5():
    sol = Solution()
    assert sol.capitalizeTitle('a') == 'a'

def test_case_6():
    sol = Solution()
    assert sol.capitalizeTitle('z') == 'z'

def test_case_7():
    sol = Solution()
    assert sol.capitalizeTitle('eLtit eHt ezIlaTipac') == 'Eltit Eht Ezilatipac'

def test_case_8():
    sol = Solution()
    assert sol.capitalizeTitle('capiTalIze tHe titLea') == 'Capitalize The Titlea'

def test_case_9():
    sol = Solution()
    assert sol.capitalizeTitle('aaaaaaaaaaaaaaaaaaaa') == 'Aaaaaaaaaaaaaaaaaaaa'

def test_case_10():
    sol = Solution()
    assert sol.capitalizeTitle('') == ''

def test_case_11():
    sol = Solution()
    assert sol.capitalizeTitle('a') == 'a'

def test_case_12():
    sol = Solution()
    assert sol.capitalizeTitle('z') == 'z'

def test_case_13():
    sol = Solution()
    assert sol.capitalizeTitle('droW HCAE fo ReTTel tsriF') == 'Drow Hcae fo Rettel Tsrif'

def test_case_14():
    sol = Solution()
    assert sol.capitalizeTitle('First leTTeR of EACH Worda') == 'First Letter of Each Worda'

def test_case_15():
    sol = Solution()
    assert sol.capitalizeTitle('aaaaaaaaaaaaaaaaaaaaaaaaa') == 'Aaaaaaaaaaaaaaaaaaaaaaaaa'

