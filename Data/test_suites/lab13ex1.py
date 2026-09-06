def test_case1():
    assert apenas_digitos_impares(468) == 0

def test_case2():
    assert apenas_digitos_impares(12426374856) == 1375

def test_case3():
    assert apenas_digitos_impares(0) == 0

def test_case4():
    assert apenas_digitos_impares(135) == 135

def test_case5():
    assert apenas_digitos_impares(246) == 0

def test_case6():
    assert apenas_digitos_impares(13579) == 13579

def test_case7():
    assert apenas_digitos_impares(2468) == 0

def test_case8():
    assert apenas_digitos_impares(1) == 1

def test_case9():
    assert apenas_digitos_impares(2) == 0

def test_case10():
    assert apenas_digitos_impares(123456789) == 13579

def test_case11():
    assert apenas_digitos_impares(98765) == 975

def test_case12():
    assert apenas_digitos_impares(10) == 1

def test_case13():
    assert apenas_digitos_impares(100) == 1

def test_case14():
    assert apenas_digitos_impares(31) == 31

def test_case15():
    assert apenas_digitos_impares(1000) == 1

def test_case16():
    assert apenas_digitos_impares(19) == 19

def test_case17():
    result = apenas_digitos_impares(135)
    assert isinstance(result, int)

def test_case18():
    assert apenas_digitos_impares(20) == 0

def test_case19():
    assert apenas_digitos_impares(5) == 5

def test_case20():
    assert apenas_digitos_impares(9876543) == 9753
