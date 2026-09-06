import pytest

def test_case1():
    assert filtra_pares((2, 5, 6, 7, 9, 1, 8, 8)) == (2, 6, 8, 8)

def test_case2():
    assert filtra_pares((1, 3, 5, 7, 9)) == ()

def test_case3():
    assert filtra_pares((0, 2, 4, 6, 8)) == (0, 2, 4, 6, 8)

def test_case4():
    assert filtra_pares((0,)) == (0,)

def test_case5():
    assert filtra_pares((1,)) == ()

def test_case6():
    assert filtra_pares(()) == ()

def test_case7():
    assert filtra_pares((1, 2, 3, 4)) == (2, 4)

def test_case8():
    assert filtra_pares((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) == (0, 2, 4, 6, 8)

def test_case9():
    assert filtra_pares((8, 8, 8)) == (8, 8, 8)

def test_case10():
    assert filtra_pares((9, 9, 9)) == ()

def test_case11():
    assert filtra_pares((2,)) == (2,)

def test_case12():
    assert filtra_pares((1, 0, 1, 0)) == (0, 0)

def test_case13():
    assert filtra_pares((3, 4, 5, 6)) == (4, 6)

def test_case14():
    assert filtra_pares((2, 2, 2)) == (2, 2, 2)

def test_case15():
    assert filtra_pares((0, 9, 8, 7, 6)) == (0, 8, 6)

def test_case16():
    with pytest.raises(ValueError):
        filtra_pares((2, 'a', 5))

def test_case17():
    with pytest.raises(ValueError):
        filtra_pares((2, -1, 5))

def test_case18():
    with pytest.raises(ValueError):
        filtra_pares((2, 10, 5))

def test_case19():
    with pytest.raises(ValueError):
        filtra_pares((1, 3.5, 2))

def test_case20():
    with pytest.raises((ValueError, TypeError)):
        filtra_pares(123)
