def test_case1():
    assert numero_digitos(0) == 1

def test_case2():
    assert numero_digitos(9) == 1

def test_case3():
    assert numero_digitos(10) == 2

def test_case4():
    assert numero_digitos(99) == 2

def test_case5():
    assert numero_digitos(100) == 3

def test_case6():
    assert numero_digitos(1012) == 4

def test_case7():
    assert numero_digitos(9999) == 4

def test_case8():
    assert numero_digitos(10000) == 5

def test_case9():
    assert numero_digitos(1) == 1

def test_case10():
    assert numero_digitos(999999) == 6

def test_case11():
    assert numero_digitos(1000000) == 7

def test_case12():
    result = numero_digitos(5)
    assert isinstance(result, int)

def test_case13():
    assert numero_digitos(11) == 2

def test_case14():
    assert numero_digitos(999) == 3

def test_case15():
    assert numero_digitos(1000) == 4

def test_case16():
    assert numero_digitos(12345) == 5

def test_case17():
    try:
        numero_digitos(-1)
        assert False, "Should raise an error for negative input"
    except (TypeError, ValueError):
        pass

def test_case18():
    try:
        numero_digitos(1.5)
        assert False, "Should raise an error for float input"
    except (TypeError, ValueError):
        pass

def test_case19():
    assert numero_digitos(50) == 2

def test_case20():
    assert numero_digitos(123456789) == 9
