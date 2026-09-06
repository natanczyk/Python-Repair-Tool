def test_case1():
    assert media_digitos(123) == 2.0

def test_case2():
    assert media_digitos(100) == 1 / 3

def test_case3():
    assert media_digitos(999) == 9.0

def test_case4():
    assert media_digitos(1) == 1.0

def test_case5():
    assert media_digitos(555) == 5.0

def test_case6():
    assert media_digitos(246) == 4.0

def test_case7():
    assert media_digitos(10) == 0.5

def test_case8():
    assert media_digitos(1000) == 0.25

def test_case9():
    assert media_digitos(12345) == 3.0

def test_case10():
    assert media_digitos(111) == 1.0

def test_case11():
    assert media_digitos(5) == 5.0

def test_case12():
    assert media_digitos(50) == 2.5

def test_case13():
    assert media_digitos(99) == 9.0

def test_case14():
    assert media_digitos(11) == 1.0

def test_case15():
    assert media_digitos(22) == 2.0

def test_case16():
    assert media_digitos(321) == 2.0

def test_case17():
    assert media_digitos(7) == 7.0

def test_case18():
    assert media_digitos(1234) == 2.5

def test_case19():
    assert media_digitos(9) == 9.0

def test_case20():
    assert media_digitos(0) == 0.0
