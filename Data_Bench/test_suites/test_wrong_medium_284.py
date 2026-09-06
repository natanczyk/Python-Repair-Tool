# Test suite for wrong_medium_284  (slug: reachable-nodes-with-restrictions)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_284.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.reachableNodes(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4

def test_case_2():
    sol = Solution()
    assert sol.reachableNodes(7, [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], [4, 2, 1]) == 3

def test_case_3():
    sol = Solution()
    assert sol.reachableNodes(0, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4

def test_case_4():
    sol = Solution()
    assert sol.reachableNodes(1, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4

def test_case_5():
    sol = Solution()
    assert sol.reachableNodes(6, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4

def test_case_6():
    sol = Solution()
    assert sol.reachableNodes(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4

def test_case_7():
    sol = Solution()
    assert sol.reachableNodes(8, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4

def test_case_8():
    sol = Solution()
    assert sol.reachableNodes(14, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4

def test_case_9():
    sol = Solution()
    assert sol.reachableNodes(17, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4

def test_case_10():
    sol = Solution()
    assert sol.reachableNodes(-1, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4

def test_case_11():
    sol = Solution()
    assert sol.reachableNodes(7, [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [4, 5]) == 1

def test_case_12():
    sol = Solution()
    assert sol.reachableNodes(7, [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [4, 5]) == 1

def test_case_13():
    sol = Solution()
    assert sol.reachableNodes(7, [[1, 0], [2, 1], [1, 3], [0, 4], [5, 0], [6, 5]], [4, 5]) == 4

def test_case_14():
    sol = Solution()
    assert sol.reachableNodes(7, [[5, 6], [0, 5], [4, 0], [3, 1], [1, 2], [0, 1]], [4, 5]) == 4

def test_case_15():
    sol = Solution()
    assert sol.reachableNodes(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], []) == 7

