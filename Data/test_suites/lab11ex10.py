def test_case1():
    assert apenas_digitos_impares(12345) == 135

def test_case2():
    assert apenas_digitos_impares(1) == 1

def test_case3():
    assert apenas_digitos_impares(9753) == 9753

def test_case4():
    assert apenas_digitos_impares(1000) == 1

def test_case5():
    assert apenas_digitos_impares(12) == 1

def test_case6():
    assert apenas_digitos_impares(23456789) == 3579

def test_case7():
    assert apenas_digitos_impares(1357) == 1357

def test_case8():
    assert apenas_digitos_impares(100003) == 13

def test_case9():
    assert apenas_digitos_impares(111) == 111

def test_case10():
    assert apenas_digitos_impares(13579) == 13579

def test_case11():
    assert apenas_digitos_impares(24681357) == 1357

def test_case12():
    result = apenas_digitos_impares(12345)
    assert isinstance(result, int)

def test_case13():
    assert apenas_digitos_impares(10203040) == 13

def test_case14():
    assert apenas_digitos_impares(123456789) == 13579

def test_case15():
    assert apenas_digitos_impares(1000000001) == 11

def test_case16():
    assert apenas_digitos_impares(21) == 1

def test_case17():
    assert apenas_digitos_impares(31) == 3

def test_case18():
    assert apenas_digitos_impares(135) == 135

def test_case19():
    assert apenas_digitos_impares(531) == 531

def test_case20():
    assert apenas_digitos_impares(9) == 9
