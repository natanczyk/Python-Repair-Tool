def test_case1():
    assert produto_digitos(12345, lambda x: x > 3) == 20

def test_case2():
    assert produto_digitos(12345, lambda x: x % 2 == 0) == 8

def test_case3():
    assert produto_digitos(246, lambda x: x > 1) == 48

def test_case4():
    assert produto_digitos(9, lambda x: x > 0) == 9

def test_case5():
    assert produto_digitos(123, lambda x: x % 2 == 1) == 3

def test_case6():
    assert produto_digitos(55, lambda x: x == 5) == 25

def test_case7():
    assert produto_digitos(2468, lambda x: x % 2 == 0) == 384

def test_case8():
    assert produto_digitos(999, lambda x: x == 9) == 729

def test_case9():
    assert produto_digitos(12, lambda x: x > 0) == 2

def test_case10():
    assert produto_digitos(123, lambda x: x > 1) == 6

def test_case11():
    assert produto_digitos(135, lambda x: x % 2 == 1) == 15

def test_case12():
    assert produto_digitos(246, lambda x: x % 2 == 0) == 48

def test_case13():
    assert produto_digitos(77, lambda x: x == 7) == 49

def test_case14():
    assert produto_digitos(12345, lambda x: x < 3) == 2

def test_case15():
    assert produto_digitos(1111, lambda x: x == 1) == 1

def test_case16():
    assert produto_digitos(369, lambda x: x % 3 == 0) == 162

def test_case17():
    assert produto_digitos(100, lambda x: x > 0) == 1

def test_case18():
    assert produto_digitos(234, lambda x: x % 2 == 0) == 8

def test_case19():
    assert produto_digitos(555, lambda x: x > 4) == 125

def test_case20():
    result = produto_digitos(12345, lambda x: x > 3)
    assert isinstance(result, int)
