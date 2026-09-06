# Test suite for wrong_medium_509  (slug: find-the-kth-largest-integer-in-the-array)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_509.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.kthLargestNumber(['3', '6', '7', '10'], 4) == '3'

def test_case_2():
    sol = Solution()
    assert sol.kthLargestNumber(['2', '21', '12', '1'], 3) == '2'

def test_case_3():
    sol = Solution()
    assert sol.kthLargestNumber(['0', '0'], 2) == '0'

def test_case_4():
    sol = Solution()
    assert sol.kthLargestNumber(['10', '3', '6', '7'], 4) == '3'

def test_case_5():
    sol = Solution()
    assert sol.kthLargestNumber(['10', '7', '6', '3'], 4) == '3'

def test_case_6():
    sol = Solution()
    assert sol.kthLargestNumber(['3', '6', '7', '10'], 0) == '3'

def test_case_7():
    sol = Solution()
    assert sol.kthLargestNumber(['3', '6', '7', '10'], 1) == '10'

def test_case_8():
    sol = Solution()
    assert sol.kthLargestNumber(['3', '6', '7', '10'], 3) == '6'

def test_case_9():
    sol = Solution()
    assert sol.kthLargestNumber(['3', '6', '7', '10'], 4) == '3'

def test_case_10():
    sol = Solution()
    assert sol.kthLargestNumber(['3', '6', '7', '10'], -1) == '6'

def test_case_11():
    sol = Solution()
    assert sol.kthLargestNumber(['1', '12', '2', '21'], 3) == '2'

def test_case_12():
    sol = Solution()
    assert sol.kthLargestNumber(['1', '12', '21', '2'], 3) == '2'

def test_case_13():
    sol = Solution()
    assert sol.kthLargestNumber(['2', '21', '12', '1'], 0) == '1'

def test_case_14():
    sol = Solution()
    assert sol.kthLargestNumber(['2', '21', '12', '1'], 1) == '21'

def test_case_15():
    sol = Solution()
    assert sol.kthLargestNumber(['2', '21', '12', '1'], 2) == '12'

