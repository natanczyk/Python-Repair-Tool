# Test suite for wrong_hard_198  (slug: count-subtrees-with-max-distance-between-cities)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_hard' / 'code' / 'wrong' / 'wrong_hard_198.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]) == [3, 4, 0]

def test_case_2():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(2, [[1, 2]]) == [1]

def test_case_3():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(3, [[1, 2], [2, 3]]) == [2, 1]

def test_case_4():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]) == [3, 4, 0]

def test_case_5():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(4, [[2, 1], [3, 2], [4, 2]]) == [3, 4, 0]

def test_case_6():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(4, [[2, 4], [2, 3], [1, 2]]) == [3, 4, 0]

def test_case_7():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(2, [[1, 2]]) == [1]

def test_case_8():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(2, [[2, 1]]) == [1]

def test_case_9():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(2, [[1, 2]]) == [1]

def test_case_10():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(3, [[1, 2], [2, 3]]) == [2, 1]

def test_case_11():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(3, [[2, 1], [3, 2]]) == [2, 1]

def test_case_12():
    sol = Solution()
    assert sol.countSubgraphsForEachDiameter(3, [[2, 3], [1, 2]]) == [2, 1]

