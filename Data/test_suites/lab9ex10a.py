import pytest

def test_case1():
    result = cria_racional(4, 6)
    assert result == {'n': 2, 'd': 3}

def test_case2():
    result = cria_racional(1, 2)
    assert result == {'n': 1, 'd': 2}

def test_case3():
    result = cria_racional(3, 9)
    assert result == {'n': 1, 'd': 3}

def test_case4():
    result = cria_racional(6, 4)
    assert result == {'n': 3, 'd': 2}

def test_case5():
    result = cria_racional(5, 1)
    assert result == {'n': 5, 'd': 1}

def test_case6():
    result = cria_racional(10, 5)
    assert result == {'n': 2, 'd': 1}

def test_case7():
    result = cria_racional(7, 7)
    assert result == {'n': 1, 'd': 1}

def test_case8():
    result = cria_racional(0, 5)
    assert result == {'n': 0, 'd': 1}

def test_case9():
    with pytest.raises(ValueError):
        cria_racional(4, 0)

def test_case10():
    with pytest.raises(ValueError):
        cria_racional(1, 0)

def test_case11():
    with pytest.raises(ValueError):
        cria_racional(4.3, 2)

def test_case12():
    with pytest.raises(ValueError):
        cria_racional(2, 3.5)

def test_case13():
    result = cria_racional(2, 3)
    assert isinstance(result, dict)
    assert 'n' in result
    assert 'd' in result

def test_case14():
    result = cria_racional(12, 8)
    assert result == {'n': 3, 'd': 2}

def test_case15():
    result = cria_racional(100, 50)
    assert result == {'n': 2, 'd': 1}

def test_case16():
    result = cria_racional(-4, 6)
    assert result['n'] == -2
    assert result['d'] == 3

def test_case17():
    result = cria_racional(4, -6)
    assert result['d'] > 0

def test_case18():
    result = cria_racional(6, 9)
    assert result == {'n': 2, 'd': 3}

def test_case19():
    result = cria_racional(15, 10)
    assert result == {'n': 3, 'd': 2}

def test_case20():
    result = cria_racional(1, 1)
    assert result == {'n': 1, 'd': 1}
