import pytest

def _f1(x):
    return -(x - 2) ** 2 + 5

def _f2(x):
    return x

def _f3(x):
    return 3

def _f4(x):
    return x ** 2

def _f5(x):
    return 2 * x

def test_case1():
    assert aproxima_area(_f1, 0.5, 3.5, 6) == pytest.approx(12.625)

def test_case2():
    assert aproxima_area(_f1, 0.5, 3.5, 12) == pytest.approx(12.71875)

def test_case3():
    assert aproxima_area(_f1, 0.5, 3.5, 100) == pytest.approx(12.749550000000003)

def test_case4():
    assert aproxima_area(_f2, 0, 2, 4) == pytest.approx(2.0)

def test_case5():
    assert aproxima_area(_f2, 1, 3, 2) == pytest.approx(4.0)

def test_case6():
    assert aproxima_area(_f2, 0, 10, 1) == pytest.approx(50.0)

def test_case7():
    assert aproxima_area(_f3, 0, 2, 1) == pytest.approx(6.0)

def test_case8():
    assert aproxima_area(_f3, 0, 5, 10) == pytest.approx(15.0)

def test_case9():
    assert aproxima_area(_f4, 0, 1, 4) == pytest.approx(0.34375)

def test_case10():
    assert aproxima_area(_f5, 0, 4, 4) == pytest.approx(16.0)

def test_case11():
    assert aproxima_area(_f3, 1, 4, 3) == pytest.approx(9.0)

def test_case12():
    assert aproxima_area(_f2, 0, 1, 1) == pytest.approx(0.5)

def test_case13():
    assert aproxima_area(_f2, 2, 4, 1) == pytest.approx(6.0)

def test_case14():
    n1 = aproxima_area(_f1, 0.5, 3.5, 6)
    n2 = aproxima_area(_f1, 0.5, 3.5, 12)
    assert n2 > n1

def test_case15():
    n2 = aproxima_area(_f1, 0.5, 3.5, 12)
    n3 = aproxima_area(_f1, 0.5, 3.5, 100)
    assert n3 > n2

def test_case16():
    assert aproxima_area(_f3, 0, 10, 5) == pytest.approx(30.0)

def test_case17():
    assert aproxima_area(_f5, 0, 2, 2) == pytest.approx(4.0)

def test_case18():
    assert aproxima_area(_f2, 0, 2, 1) == pytest.approx(2.0)

def test_case19():
    result = aproxima_area(_f1, 0.5, 3.5, 1000)
    assert result == pytest.approx(12.75, rel=1e-3)

def test_case20():
    assert aproxima_area(_f4, 0, 2, 2) == pytest.approx(2.5)
