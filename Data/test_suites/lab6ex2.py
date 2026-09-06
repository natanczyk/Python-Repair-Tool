import pytest

def test_case1():
    assert explode(34500) == (3, 4, 5, 0, 0)

def test_case2():
    assert explode(1) == (1,)

def test_case3():
    assert explode(123) == (1, 2, 3)

def test_case4():
    assert explode(1000) == (1, 0, 0, 0)

def test_case5():
    assert explode(9) == (9,)

def test_case6():
    assert explode(10) == (1, 0)

def test_case7():
    assert explode(100) == (1, 0, 0)

def test_case8():
    assert explode(9999) == (9, 9, 9, 9)

def test_case9():
    assert explode(123456789) == (1, 2, 3, 4, 5, 6, 7, 8, 9)

def test_case10():
    assert explode(1001) == (1, 0, 0, 1)

def test_case11():
    assert explode(500) == (5, 0, 0)

def test_case12():
    assert explode(20) == (2, 0)

def test_case13():
    assert explode(999) == (9, 9, 9)

def test_case14():
    assert explode(10000) == (1, 0, 0, 0, 0)

def test_case15():
    assert explode(12) == (1, 2)

def test_case16():
    with pytest.raises(ValueError):
        explode(3.5)

def test_case17():
    with pytest.raises(ValueError):
        explode(0)

def test_case18():
    with pytest.raises(ValueError):
        explode(-5)

def test_case19():
    with pytest.raises(ValueError):
        explode(-1)

def test_case20():
    with pytest.raises((ValueError, TypeError)):
        explode('hello')
