def test_case1():
    assert soma_n_vezes(3, 2, 5) == 17

def test_case2():
    assert soma_n_vezes(1, 0, 5) == 5

def test_case3():
    assert soma_n_vezes(0, 5, 3) == 5

def test_case4():
    assert soma_n_vezes(2, 3, 0) == 3

def test_case5():
    assert soma_n_vezes(5, 0, 0) == 0

def test_case6():
    assert soma_n_vezes(1, 1, 1) == 2

def test_case7():
    assert soma_n_vezes(4, 4, 4) == 20

def test_case8():
    assert soma_n_vezes(3, 0, 3) == 9

def test_case9():
    assert soma_n_vezes(10, 5, 2) == 25

def test_case10():
    assert soma_n_vezes(6, 1, 4) == 25

def test_case11():
    assert soma_n_vezes(1, 0, 0) == 0

def test_case12():
    assert soma_n_vezes(0, 0, 0) == 0

def test_case13():
    assert soma_n_vezes(7, 3, 2) == 17

def test_case14():
    assert soma_n_vezes(2, 2, 2) == 6

def test_case15():
    assert soma_n_vezes(5, 5, 5) == 30

def test_case16():
    assert soma_n_vezes(1, 0, 10) == 10

def test_case17():
    assert soma_n_vezes(10, 0, 1) == 10

def test_case18():
    result = soma_n_vezes(3, 2, 5)
    assert isinstance(result, int)

def test_case19():
    assert soma_n_vezes(2, 1, 3) == 7

def test_case20():
    assert soma_n_vezes(4, 0, 5) == 20
