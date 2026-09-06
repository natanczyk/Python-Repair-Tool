def test_case1():
    assert soma_divisores(1) == 1

def test_case2():
    assert soma_divisores(2) == 3

def test_case3():
    assert soma_divisores(3) == 4

def test_case4():
    assert soma_divisores(4) == 7

def test_case5():
    assert soma_divisores(5) == 6

def test_case6():
    assert soma_divisores(6) == 12

def test_case7():
    assert soma_divisores(7) == 8

def test_case8():
    assert soma_divisores(8) == 15

def test_case9():
    assert soma_divisores(9) == 13

def test_case10():
    assert soma_divisores(10) == 18

def test_case11():
    assert soma_divisores(12) == 28

def test_case12():
    result = soma_divisores(6)
    assert isinstance(result, int)

def test_case13():
    assert soma_divisores(15) == 24

def test_case14():
    assert soma_divisores(16) == 31

def test_case15():
    assert soma_divisores(28) == 56

def test_case16():
    assert soma_divisores(100) == 217

def test_case17():
    assert soma_divisores(24) == 60

def test_case18():
    assert soma_divisores(36) == 91

def test_case19():
    assert soma_divisores(17) == 18

def test_case20():
    assert soma_divisores(20) == 42
