def test_case1():
    assert maior_inteiro(1) == 1

def test_case2():
    assert maior_inteiro(2) == 1

def test_case3():
    assert maior_inteiro(3) == 2

def test_case4():
    assert maior_inteiro(4) == 2

def test_case5():
    assert maior_inteiro(5) == 2

def test_case6():
    assert maior_inteiro(6) == 3

def test_case7():
    assert maior_inteiro(7) == 3

def test_case8():
    assert maior_inteiro(9) == 3

def test_case9():
    assert maior_inteiro(10) == 4

def test_case10():
    assert maior_inteiro(14) == 4

def test_case11():
    assert maior_inteiro(15) == 5

def test_case12():
    result = maior_inteiro(6)
    assert isinstance(result, int)

def test_case13():
    assert maior_inteiro(20) == 5

def test_case14():
    assert maior_inteiro(21) == 6

def test_case15():
    assert maior_inteiro(27) == 6

def test_case16():
    assert maior_inteiro(28) == 7

def test_case17():
    assert maior_inteiro(50) == 9

def test_case18():
    assert maior_inteiro(45) == 9

def test_case19():
    assert maior_inteiro(100) == 13

def test_case20():
    assert maior_inteiro(91) == 13
