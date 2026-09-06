def test_case1():
    result = produtorio(1, 5, lambda x: x, lambda x: x + 1)
    assert result == 120

def test_case2():
    result = produtorio(1, 4, lambda x: x, lambda x: x + 1)
    assert result == 24

def test_case3():
    result = produtorio(2, 5, lambda x: x, lambda x: x + 1)
    assert result == 120

def test_case4():
    result = produtorio(3, 3, lambda x: x, lambda x: x + 1)
    assert result == 3

def test_case5():
    result = produtorio(1, 10, lambda x: x, lambda x: x + 1)
    assert result == 3628800

def test_case6():
    result = produtorio(5, 4, lambda x: x, lambda x: x + 1)
    assert result == 1

def test_case7():
    result = produtorio(1, 4, lambda x: x ** 2, lambda x: x + 1)
    assert result == 576

def test_case8():
    result = produtorio(2, 8, lambda x: x, lambda x: x + 2)
    assert result == 384

def test_case9():
    result = produtorio(1, 3, lambda x: x ** 3, lambda x: x + 1)
    assert result == 216

def test_case10():
    result = produtorio(1, 6, lambda x: x, lambda x: x + 1)
    assert result == 720

def test_case11():
    result = produtorio(1, 1, lambda x: x, lambda x: x + 1)
    assert result == 1

def test_case12():
    result = produtorio(2, 4, lambda x: x, lambda x: x + 1)
    assert result == 24

def test_case13():
    result = produtorio(1, 5, lambda x: x ** 2, lambda x: x + 1)
    assert result == 14400

def test_case14():
    result = produtorio(1, 7, lambda x: x, lambda x: x + 1)
    assert result == 5040

def test_case15():
    result = produtorio(2, 6, lambda x: x, lambda x: x + 2)
    assert result == 48

def test_case16():
    result = produtorio(3, 9, lambda x: x, lambda x: x + 3)
    assert result == 162

def test_case17():
    result = produtorio(1, 2, lambda x: x, lambda x: x + 1)
    assert result == 2

def test_case18():
    result = produtorio(10, 9, lambda x: x, lambda x: x + 1)
    assert result == 1

def test_case19():
    result = produtorio(1, 3, lambda x: 2, lambda x: x + 1)
    assert result == 8

def test_case20():
    result = produtorio(1, 4, lambda x: 3, lambda x: x + 1)
    assert result == 81
