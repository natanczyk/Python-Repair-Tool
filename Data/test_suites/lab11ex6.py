def test_case1():
    assert nao_primos(8) == [1, 4, 6, 8]

def test_case2():
    assert nao_primos(1) == [1]

def test_case3():
    assert nao_primos(2) == [1]

def test_case4():
    assert nao_primos(4) == [1, 4]

def test_case5():
    assert nao_primos(6) == [1, 4, 6]

def test_case6():
    assert nao_primos(10) == [1, 4, 6, 8, 9, 10]

def test_case7():
    assert nao_primos(12) == [1, 4, 6, 8, 9, 10, 12]

def test_case8():
    assert nao_primos(9) == [1, 4, 6, 8, 9]

def test_case9():
    result = nao_primos(8)
    assert isinstance(result, list)

def test_case10():
    assert 2 not in nao_primos(10)

def test_case11():
    assert 3 not in nao_primos(10)

def test_case12():
    assert 5 not in nao_primos(10)

def test_case13():
    assert 7 not in nao_primos(10)

def test_case14():
    assert 1 in nao_primos(10)

def test_case15():
    result = nao_primos(20)
    assert result == [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

def test_case16():
    assert nao_primos(3) == [1]

def test_case17():
    assert len(nao_primos(10)) == 6

def test_case18():
    assert nao_primos(15) == [1, 4, 6, 8, 9, 10, 12, 14, 15]

def test_case19():
    result = nao_primos(5)
    assert result == [1, 4]

def test_case20():
    assert 11 not in nao_primos(20)
