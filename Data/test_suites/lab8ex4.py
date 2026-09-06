import pytest

def test_case1():
    assert elemento_matriz([[1, 2, 3], [4, 5, 6]], 0, 0) == 1

def test_case2():
    assert elemento_matriz([[1, 2, 3], [4, 5, 6]], 0, 1) == 2

def test_case3():
    assert elemento_matriz([[1, 2, 3], [4, 5, 6]], 0, 2) == 3

def test_case4():
    assert elemento_matriz([[1, 2, 3], [4, 5, 6]], 1, 0) == 4

def test_case5():
    assert elemento_matriz([[1, 2, 3], [4, 5, 6]], 1, 1) == 5

def test_case6():
    assert elemento_matriz([[1, 2, 3], [4, 5, 6]], 1, 2) == 6

def test_case7():
    assert elemento_matriz([[10, 20], [30, 40], [50, 60]], 0, 0) == 10

def test_case8():
    assert elemento_matriz([[10, 20], [30, 40], [50, 60]], 2, 1) == 60

def test_case9():
    assert elemento_matriz([[10, 20], [30, 40], [50, 60]], 1, 1) == 40

def test_case10():
    assert elemento_matriz([[7]], 0, 0) == 7

def test_case11():
    assert elemento_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2) == 9

def test_case12():
    assert elemento_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1) == 5

def test_case13():
    assert elemento_matriz([[0, 0], [0, 0]], 0, 0) == 0

def test_case14():
    assert elemento_matriz([[-1, -2], [-3, -4]], 1, 0) == -3

def test_case15():
    assert elemento_matriz([[100, 200], [300, 400]], 0, 1) == 200

def test_case16():
    with pytest.raises(ValueError):
        elemento_matriz([[1, 2, 3], [4, 5, 6]], 0, 3)

def test_case17():
    with pytest.raises(ValueError):
        elemento_matriz([[1, 2, 3], [4, 5, 6]], 2, 0)

def test_case18():
    with pytest.raises(ValueError):
        elemento_matriz([[1, 2], [3, 4]], 0, 2)

def test_case19():
    with pytest.raises(ValueError):
        elemento_matriz([[1, 2], [3, 4]], 3, 0)

def test_case20():
    with pytest.raises(ValueError):
        elemento_matriz([[7]], 1, 0)
