def test_case1():
    assert posicoes_maximo((1, 2, 3, 2, 1, 2, 3)) == (2, 6)

def test_case2():
    assert posicoes_maximo((5,)) == (0,)

def test_case3():
    assert posicoes_maximo((1, 1, 1)) == (0, 1, 2)

def test_case4():
    assert posicoes_maximo((3, 1, 3, 1, 3)) == (0, 2, 4)

def test_case5():
    assert posicoes_maximo((1, 2, 3)) == (2,)

def test_case6():
    assert posicoes_maximo((-1, -2, -3)) == (0,)

def test_case7():
    assert posicoes_maximo((0, 0, 0)) == (0, 1, 2)

def test_case8():
    assert posicoes_maximo((1,)) == (0,)

def test_case9():
    assert posicoes_maximo((1, 3, 5, 3, 1)) == (2,)

def test_case10():
    assert posicoes_maximo((5, 5, 3)) == (0, 1)

def test_case11():
    assert posicoes_maximo((1, 2)) == (1,)

def test_case12():
    assert posicoes_maximo((2, 1)) == (0,)

def test_case13():
    assert posicoes_maximo((4, 1, 4, 1, 4)) == (0, 2, 4)

def test_case14():
    assert posicoes_maximo((10, 20, 10)) == (1,)

def test_case15():
    assert posicoes_maximo((7, 7, 7, 7)) == (0, 1, 2, 3)

def test_case16():
    assert posicoes_maximo((0, 1, 0)) == (1,)

def test_case17():
    assert posicoes_maximo((3, 3, 1, 3)) == (0, 1, 3)

def test_case18():
    assert posicoes_maximo((100, 50, 75)) == (0,)

def test_case19():
    assert posicoes_maximo((-5, -1, -3, -1)) == (1, 3)

def test_case20():
    assert posicoes_maximo((2, 2)) == (0, 1)
