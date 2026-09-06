def test_case1():
    r1 = {'n': 2, 'd': 3}
    r2 = {'n': 2, 'd': 3}
    result = prod_racionais(r1, r2)
    assert result == {'n': 4, 'd': 9}

def test_case2():
    r1 = {'n': 2, 'd': 3}
    r2 = {'n': 3, 'd': 4}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 2}

def test_case3():
    r1 = {'n': 1, 'd': 2}
    r2 = {'n': 1, 'd': 2}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 4}

def test_case4():
    r1 = {'n': 3, 'd': 4}
    r2 = {'n': 2, 'd': 3}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 2}

def test_case5():
    r1 = {'n': 1, 'd': 3}
    r2 = {'n': 3, 'd': 1}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 1}

def test_case6():
    r1 = {'n': 0, 'd': 1}
    r2 = {'n': 5, 'd': 7}
    result = prod_racionais(r1, r2)
    assert result == {'n': 0, 'd': 1}

def test_case7():
    r1 = {'n': 1, 'd': 1}
    r2 = {'n': 1, 'd': 1}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 1}

def test_case8():
    r1 = {'n': 2, 'd': 5}
    r2 = {'n': 5, 'd': 2}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 1}

def test_case9():
    r1 = {'n': 1, 'd': 4}
    r2 = {'n': 2, 'd': 1}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 2}

def test_case10():
    r1 = {'n': 3, 'd': 5}
    r2 = {'n': 5, 'd': 9}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 3}

def test_case11():
    r1 = {'n': 1, 'd': 2}
    r2 = {'n': 4, 'd': 1}
    result = prod_racionais(r1, r2)
    assert result == {'n': 2, 'd': 1}

def test_case12():
    r1 = {'n': 7, 'd': 8}
    r2 = {'n': 8, 'd': 7}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 1}

def test_case13():
    r1 = {'n': 3, 'd': 7}
    r2 = {'n': 7, 'd': 3}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 1}

def test_case14():
    r1 = {'n': 2, 'd': 9}
    r2 = {'n': 3, 'd': 4}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 6}

def test_case15():
    r1 = {'n': 5, 'd': 6}
    r2 = {'n': 3, 'd': 10}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 4}

def test_case16():
    r1 = {'n': 4, 'd': 5}
    r2 = {'n': 5, 'd': 4}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 1}

def test_case17():
    r1 = {'n': 1, 'd': 6}
    r2 = {'n': 6, 'd': 1}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 1}

def test_case18():
    r1 = {'n': 2, 'd': 3}
    r2 = {'n': 1, 'd': 2}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 3}

def test_case19():
    r1 = {'n': 3, 'd': 8}
    r2 = {'n': 4, 'd': 9}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 6}

def test_case20():
    r1 = {'n': 5, 'd': 12}
    r2 = {'n': 4, 'd': 15}
    result = prod_racionais(r1, r2)
    assert result == {'n': 1, 'd': 9}
