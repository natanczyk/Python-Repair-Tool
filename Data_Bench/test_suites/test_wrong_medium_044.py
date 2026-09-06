# Test suite for wrong_medium_044  (slug: partition-labels)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_044.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.partitionLabels('ababcbacadefegdehijhklij') == [9, 7, 8]

def test_case_2():
    sol = Solution()
    assert sol.partitionLabels('eccbbbbdec') == [10]

def test_case_3():
    sol = Solution()
    assert sol.partitionLabels('') == []

def test_case_4():
    sol = Solution()
    assert sol.partitionLabels('a') == [1]

def test_case_5():
    sol = Solution()
    assert sol.partitionLabels('z') == [1]

def test_case_6():
    sol = Solution()
    assert sol.partitionLabels('jilkhjihedgefedacabcbaba') == [8, 7, 9]

def test_case_7():
    sol = Solution()
    assert sol.partitionLabels('ababcbacadefegdehijhklija') == [25]

def test_case_8():
    sol = Solution()
    assert sol.partitionLabels('aaaaaaaaaaaaaaaaaaaaaaaa') == [24]

def test_case_9():
    sol = Solution()
    assert sol.partitionLabels('') == []

def test_case_10():
    sol = Solution()
    assert sol.partitionLabels('a') == [1]

def test_case_11():
    sol = Solution()
    assert sol.partitionLabels('z') == [1]

def test_case_12():
    sol = Solution()
    assert sol.partitionLabels('cedbbbbcce') == [10]

def test_case_13():
    sol = Solution()
    assert sol.partitionLabels('eccbbbbdeca') == [10, 1]

def test_case_14():
    sol = Solution()
    assert sol.partitionLabels('aaaaaaaaaa') == [10]

