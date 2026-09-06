# Auto-generated test for wrong_hard_468  (slug: substring-with-concatenation-of-all-words)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_468.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.findSubstring("barfoothefoobarman", ["foo","bar"])
    assert result == [0,9]

def test_case_2():
    sol = Solution()
    result = sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])
    assert result == []

def test_case_3():
    sol = Solution()
    result = sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
    assert result == [6,9,12]

