import pytest

def test_case1():
    assert area_coroa(1, 2) == 3.14 * 2 * 2 - 3.14 * 1 * 1

def test_case2():
    assert area_coroa(0, 3) == 3.14 * 3 * 3

def test_case3():
    assert area_coroa(2, 5) == 3.14 * 5 * 5 - 3.14 * 2 * 2

def test_case4():
    assert area_coroa(1, 1) == 0.0

def test_case5():
    assert area_coroa(0, 1) == 3.14

def test_case6():
    assert area_coroa(3, 10) == 3.14 * 10 * 10 - 3.14 * 3 * 3

def test_case7():
    assert area_coroa(0, 5) == 3.14 * 5 * 5

def test_case8():
    assert area_coroa(1, 3) == 3.14 * 3 * 3 - 3.14 * 1 * 1

def test_case9():
    assert area_coroa(2, 4) == 3.14 * 4 * 4 - 3.14 * 2 * 2

def test_case10():
    assert area_coroa(5, 10) == 3.14 * 10 * 10 - 3.14 * 5 * 5

def test_case11():
    assert area_coroa(0, 10) == 3.14 * 10 * 10

def test_case12():
    assert area_coroa(1, 4) == 3.14 * 4 * 4 - 3.14 * 1 * 1

def test_case13():
    assert area_coroa(3, 5) == 3.14 * 5 * 5 - 3.14 * 3 * 3

def test_case14():
    assert area_coroa(0, 2) == 3.14 * 2 * 2

def test_case15():
    assert area_coroa(4, 6) == 3.14 * 6 * 6 - 3.14 * 4 * 4

def test_case16():
    assert area_coroa(1, 10) == 3.14 * 10 * 10 - 3.14 * 1 * 1

def test_case17():
    with pytest.raises(ValueError):
        area_coroa(3, 1)

def test_case18():
    with pytest.raises(ValueError):
        area_coroa(5, 2)

def test_case19():
    with pytest.raises(ValueError):
        area_coroa(10, 3)

def test_case20():
    with pytest.raises(ValueError):
        area_coroa(2, 1)
