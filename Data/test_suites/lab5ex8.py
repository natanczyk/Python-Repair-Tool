import pytest

def test_case1():
    assert serie_geom(2, 4) == 31

def test_case2():
    assert serie_geom(100, 0) == 1

def test_case3():
    assert serie_geom(1, 5) == 6

def test_case4():
    assert serie_geom(3, 3) == 40

def test_case5():
    assert serie_geom(0, 5) == 1

def test_case6():
    assert serie_geom(-1, 4) == 1

def test_case7():
    assert serie_geom(-1, 5) == 0

def test_case8():
    assert serie_geom(2, 0) == 1

def test_case9():
    assert serie_geom(2, 1) == 3

def test_case10():
    assert serie_geom(10, 2) == 111

def test_case11():
    assert serie_geom(5, 3) == 156

def test_case12():
    assert serie_geom(-2, 3) == -5

def test_case13():
    assert serie_geom(3, 0) == 1

def test_case14():
    assert serie_geom(2, 10) == 2047

def test_case15():
    assert serie_geom(4, 2) == 21

def test_case16():
    assert serie_geom(7, 2) == 57

def test_case17():
    assert serie_geom(10, 3) == 1111

def test_case18():
    with pytest.raises(ValueError):
        serie_geom(100, -1)

def test_case19():
    with pytest.raises(ValueError):
        serie_geom(2, -5)

def test_case20():
    with pytest.raises(ValueError):
        serie_geom(0, -1)
