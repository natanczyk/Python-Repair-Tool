def test_case1():
    assert eh_capicua(1) == True

def test_case2():
    assert eh_capicua(9) == True

def test_case3():
    assert eh_capicua(11) == True

def test_case4():
    assert eh_capicua(12) == False

def test_case5():
    assert eh_capicua(121) == True

def test_case6():
    assert eh_capicua(123) == False

def test_case7():
    assert eh_capicua(1221) == True

def test_case8():
    assert eh_capicua(12321) == True

def test_case9():
    assert eh_capicua(123210) == False

def test_case10():
    assert eh_capicua(10001) == True

def test_case11():
    assert eh_capicua(10101) == True

def test_case12():
    result = eh_capicua(5)
    assert isinstance(result, bool)

def test_case13():
    assert eh_capicua(99) == True

def test_case14():
    assert eh_capicua(100) == False

def test_case15():
    assert eh_capicua(9009) == True

def test_case16():
    assert eh_capicua(9119) == True

def test_case17():
    assert eh_capicua(1234) == False

def test_case18():
    assert eh_capicua(12221) == True

def test_case19():
    assert eh_capicua(99999) == True

def test_case20():
    assert eh_capicua(123321) == True
