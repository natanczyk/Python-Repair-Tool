import pytest

def test_case1():
    notas = {1: [46592, 49212, 90300, 59312], 15: [52592, 59212], 20: [58323]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(50 / 3)
    assert failed == 4

def test_case2():
    notas = {10: [1, 2, 3]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(10.0)
    assert failed == 0

def test_case3():
    notas = {9: [1], 10: [2]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(10.0)
    assert failed == 1

def test_case4():
    notas = {5: [1, 2], 15: [3]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(15.0)
    assert failed == 2

def test_case5():
    notas = {0: [1, 2, 3, 4, 5], 20: [6]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(20.0)
    assert failed == 5

def test_case6():
    notas = {20: [1, 2]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(20.0)
    assert failed == 0

def test_case7():
    notas = {10: [1], 15: [2], 20: [3]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(15.0)
    assert failed == 0

def test_case8():
    notas = {5: [1, 2, 3], 10: [4, 5, 6]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(10.0)
    assert failed == 3

def test_case9():
    notas = {1: [1], 19: [2]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(19.0)
    assert failed == 1

def test_case10():
    notas = {10: [1], 20: [2]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(15.0)
    assert failed == 0

def test_case11():
    notas = {1: [1, 2, 3, 4, 5]}
    _, failed = resumo_FP(notas)
    assert failed == 5

def test_case12():
    notas = {12: [1, 2], 18: [3, 4]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(15.0)
    assert failed == 0

def test_case13():
    notas = {9: [1, 2, 3], 11: [4], 20: [5]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx((11 + 20) / 2)
    assert failed == 3

def test_case14():
    notas = {10: [1, 2, 3], 11: [4, 5]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx((10 * 3 + 11 * 2) / 5)
    assert failed == 0

def test_case15():
    notas = {0: [1], 10: [2], 20: [3]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(15.0)
    assert failed == 1

def test_case16():
    notas = {1: [1, 2, 3, 4, 5], 15: [6], 20: [7]}
    _, failed = resumo_FP(notas)
    assert failed == 5

def test_case17():
    notas = {10: [1]}
    result = resumo_FP(notas)
    assert isinstance(result, tuple)
    assert len(result) == 2

def test_case18():
    notas = {1: [1, 2], 9: [3], 10: [4], 15: [5, 6]}
    _, failed = resumo_FP(notas)
    assert failed == 3

def test_case19():
    notas = {14: [1, 2, 3]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx(14.0)
    assert failed == 0

def test_case20():
    notas = {5: [1], 8: [2], 10: [3], 16: [4]}
    avg, failed = resumo_FP(notas)
    assert avg == pytest.approx((10 + 16) / 2)
    assert failed == 2
