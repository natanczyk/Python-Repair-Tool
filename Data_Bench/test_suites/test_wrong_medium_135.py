# Test suite for wrong_medium_135  (slug: making-file-names-unique)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_135.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.getFolderNames([]) == []

def test_case_2():
    sol = Solution()
    assert sol.getFolderNames(['pes']) == ['pes']

def test_case_3():
    sol = Solution()
    assert sol.getFolderNames(['fifa', 'gta', 'pes', 'pes(2019)']) == ['fifa', 'gta', 'pes', 'pes(2019)']

def test_case_4():
    sol = Solution()
    assert sol.getFolderNames(['pes(2019)', 'gta', 'fifa', 'pes']) == ['pes(2019)', 'gta', 'fifa', 'pes']

def test_case_5():
    sol = Solution()
    assert sol.getFolderNames(['pes', 'fifa', 'gta', 'pes(2019)', 'x']) == ['pes', 'fifa', 'gta', 'pes(2019)', 'x']

def test_case_6():
    sol = Solution()
    assert sol.getFolderNames([]) == []

def test_case_7():
    sol = Solution()
    assert sol.getFolderNames(['gta']) == ['gta']

def test_case_8():
    sol = Solution()
    assert sol.getFolderNames(['avalon', 'gta', 'gta', 'gta(1)']) == ['avalon', 'gta', 'gta(1)', 'gta(1)(1)']

def test_case_9():
    sol = Solution()
    assert sol.getFolderNames(['avalon', 'gta', 'gta(1)', 'gta']) == ['avalon', 'gta', 'gta(1)', 'gta(2)']

def test_case_10():
    sol = Solution()
    assert sol.getFolderNames(['gta', 'gta(1)', 'gta', 'avalon', 'x']) == ['gta', 'gta(1)', 'gta(2)', 'avalon', 'x']

def test_case_11():
    sol = Solution()
    assert sol.getFolderNames([]) == []

def test_case_12():
    sol = Solution()
    assert sol.getFolderNames(['onepiece']) == ['onepiece']

def test_case_13():
    sol = Solution()
    assert sol.getFolderNames(['onepiece', 'onepiece', 'onepiece(1)', 'onepiece(2)', 'onepiece(3)']) == ['onepiece', 'onepiece(1)', 'onepiece(1)(1)', 'onepiece(2)', 'onepiece(3)']

def test_case_14():
    sol = Solution()
    assert sol.getFolderNames(['onepiece', 'onepiece(3)', 'onepiece(2)', 'onepiece(1)', 'onepiece']) == ['onepiece', 'onepiece(3)', 'onepiece(2)', 'onepiece(1)', 'onepiece(4)']

def test_case_15():
    sol = Solution()
    assert sol.getFolderNames(['onepiece', 'onepiece(1)', 'onepiece(2)', 'onepiece(3)', 'onepiece', 'x']) == ['onepiece', 'onepiece(1)', 'onepiece(2)', 'onepiece(3)', 'onepiece(4)', 'x']

