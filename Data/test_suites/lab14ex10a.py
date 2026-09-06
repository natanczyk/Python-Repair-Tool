def test_case1():
    assert perfeito(1) == False

def test_case2():
    assert perfeito(2) == False

def test_case3():
    assert perfeito(3) == False

def test_case4():
    assert perfeito(4) == False

def test_case5():
    assert perfeito(5) == False

def test_case6():
    assert perfeito(6) == True

def test_case7():
    assert perfeito(7) == False

def test_case8():
    assert perfeito(12) == False

def test_case9():
    assert perfeito(28) == True

def test_case10():
    assert perfeito(100) == False

def test_case11():
    result = perfeito(6)
    assert isinstance(result, bool)

def test_case12():
    assert perfeito(496) == True

def test_case13():
    assert perfeito(10) == False

def test_case14():
    assert perfeito(8) == False

def test_case15():
    assert perfeito(9) == False

def test_case16():
    assert perfeito(15) == False

def test_case17():
    assert perfeito(16) == False

def test_case18():
    assert perfeito(20) == False

def test_case19():
    assert perfeito(27) == False

def test_case20():
    assert perfeito(8128) == True
