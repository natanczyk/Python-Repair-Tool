# Auto-generated test for wrong_hard_168  (slug: number-of-ways-of-cutting-a-pizza)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_168.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    result = sol.ways(["A..","AAA","..."], 3)
    assert result == 3

def test_case_2():
    sol = Solution()
    result = sol.ways(["A..","AA.","..."], 3)
    assert result == 1

def test_case_3():
    sol = Solution()
    result = sol.ways(["A..","A..","..."], 1)
    assert result == 1

