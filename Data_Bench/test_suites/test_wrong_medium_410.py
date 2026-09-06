# Test suite for wrong_medium_410  (slug: restore-ip-addresses)
import importlib.util, pathlib

_wrong_path = (
    pathlib.Path(__file__).parent.parent
    / 'question_medium' / 'code' / 'wrong' / 'wrong_medium_410.py'
)
_spec = importlib.util.spec_from_file_location('_sol', _wrong_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Solution = _mod.Solution

def test_case_1():
    sol = Solution()
    assert sol.restoreIpAddresses('25525511135') == ['255.255.11.135', '255.255.111.35']

def test_case_2():
    sol = Solution()
    assert sol.restoreIpAddresses('0000') == ['0.0.0.0']

def test_case_3():
    sol = Solution()
    assert sol.restoreIpAddresses('101023') == ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']

def test_case_4():
    sol = Solution()
    assert sol.restoreIpAddresses('') == []

def test_case_5():
    sol = Solution()
    assert sol.restoreIpAddresses('53111552552') == []

def test_case_6():
    sol = Solution()
    assert sol.restoreIpAddresses('') == []

def test_case_7():
    sol = Solution()
    assert sol.restoreIpAddresses('0000') == ['0.0.0.0']

def test_case_8():
    sol = Solution()
    assert sol.restoreIpAddresses('') == []

def test_case_9():
    sol = Solution()
    assert sol.restoreIpAddresses('320101') == ['3.2.0.101', '3.20.10.1', '3.201.0.1', '32.0.10.1']

