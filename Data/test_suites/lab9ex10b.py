def test_case1():
    r = {'n': 2, 'd': 3}
    assert escreve_racional(r) == '2/3'

def test_case2():
    r = {'n': 5, 'd': 1}
    assert escreve_racional(r) == '5'

def test_case3():
    r = {'n': 1, 'd': 2}
    assert escreve_racional(r) == '1/2'

def test_case4():
    r = {'n': 3, 'd': 1}
    assert escreve_racional(r) == '3'

def test_case5():
    r = {'n': 7, 'd': 4}
    assert escreve_racional(r) == '7/4'

def test_case6():
    r = {'n': 0, 'd': 1}
    assert escreve_racional(r) == '0'

def test_case7():
    r = {'n': 1, 'd': 1}
    assert escreve_racional(r) == '1'

def test_case8():
    r = {'n': 3, 'd': 7}
    assert escreve_racional(r) == '3/7'

def test_case9():
    r = {'n': -2, 'd': 3}
    assert escreve_racional(r) == '-2/3'

def test_case10():
    r = {'n': -5, 'd': 1}
    assert escreve_racional(r) == '-5'

def test_case11():
    r = {'n': 10, 'd': 3}
    result = escreve_racional(r)
    assert isinstance(result, str)

def test_case12():
    r = {'n': 4, 'd': 1}
    assert '/' not in escreve_racional(r)

def test_case13():
    r = {'n': 4, 'd': 3}
    assert '/' in escreve_racional(r)

def test_case14():
    r = {'n': 1, 'd': 4}
    assert escreve_racional(r) == '1/4'

def test_case15():
    r = {'n': 100, 'd': 1}
    assert escreve_racional(r) == '100'

def test_case16():
    r = {'n': 99, 'd': 100}
    assert escreve_racional(r) == '99/100'

def test_case17():
    r = {'n': 2, 'd': 1}
    assert escreve_racional(r) == '2'

def test_case18():
    r = {'n': 13, 'd': 7}
    assert escreve_racional(r) == '13/7'

def test_case19():
    r = {'n': 0, 'd': 5}
    result = escreve_racional(r)
    assert '0' in result

def test_case20():
    r = {'n': 1, 'd': 1000}
    assert escreve_racional(r) == '1/1000'
