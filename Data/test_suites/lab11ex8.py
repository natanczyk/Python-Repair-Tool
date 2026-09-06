def test_case1():
    assert lista_digitos(123) == [1, 2, 3]

def test_case2():
    assert lista_digitos(1) == [1]

def test_case3():
    assert lista_digitos(9) == [9]

def test_case4():
    assert lista_digitos(10) == [1, 0]

def test_case5():
    assert lista_digitos(100) == [1, 0, 0]

def test_case6():
    assert lista_digitos(1000) == [1, 0, 0, 0]

def test_case7():
    assert lista_digitos(12345) == [1, 2, 3, 4, 5]

def test_case8():
    assert lista_digitos(98765) == [9, 8, 7, 6, 5]

def test_case9():
    result = lista_digitos(123)
    assert isinstance(result, list)

def test_case10():
    assert all(isinstance(d, int) for d in lista_digitos(123))

def test_case11():
    assert lista_digitos(5) == [5]

def test_case12():
    assert lista_digitos(50) == [5, 0]

def test_case13():
    assert len(lista_digitos(12345)) == 5

def test_case14():
    assert len(lista_digitos(1)) == 1

def test_case15():
    assert len(lista_digitos(10000)) == 5

def test_case16():
    assert lista_digitos(999) == [9, 9, 9]

def test_case17():
    assert lista_digitos(1234567890) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def test_case18():
    assert lista_digitos(20) == [2, 0]

def test_case19():
    assert lista_digitos(321) == [3, 2, 1]

def test_case20():
    assert lista_digitos(2) == [2]
