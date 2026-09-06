# Test suite for wrong_medium_173  (slug: partition-string-into-substrings-with-values-at-most-k)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_173.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.minimumPartition('', 60) == 1

def test_case_2():
    sol = Solution()
    assert sol.minimumPartition('264561', 60) == 4

def test_case_3():
    sol = Solution()
    assert sol.minimumPartition('165462', 0) == -1

def test_case_4():
    sol = Solution()
    assert sol.minimumPartition('165462', 1) == -1

def test_case_5():
    sol = Solution()
    assert sol.minimumPartition('165462', 70) == 3

def test_case_6():
    sol = Solution()
    assert sol.minimumPartition('165462', 120) == 3

def test_case_7():
    sol = Solution()
    assert sol.minimumPartition('165462', 59) == 4

def test_case_8():
    sol = Solution()
    assert sol.minimumPartition('165462', 60) == 4

def test_case_9():
    sol = Solution()
    assert sol.minimumPartition('165462', 61) == 4

def test_case_10():
    sol = Solution()
    assert sol.minimumPartition('165462', -1) == -1

def test_case_11():
    sol = Solution()
    assert sol.minimumPartition('', 5) == 1

def test_case_12():
    sol = Solution()
    assert sol.minimumPartition('281832', 5) == -1

def test_case_13():
    sol = Solution()
    assert sol.minimumPartition('238182a', 5) == -1

def test_case_14():
    sol = Solution()
    assert sol.minimumPartition('238182', 0) == -1

def test_case_15():
    sol = Solution()
    assert sol.minimumPartition('238182', 1) == -1

