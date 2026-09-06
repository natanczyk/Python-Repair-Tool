def test_case1():
    assert reconhece('A1') == True

def test_case2():
    assert reconhece('ABBBBCDDDD23311') == True

def test_case3():
    assert reconhece('ABC12C') == False

def test_case4():
    assert reconhece('ABCD1234') == True

def test_case5():
    assert reconhece('D4') == True

def test_case6():
    assert reconhece('DDDD1') == True

def test_case7():
    assert reconhece('A1234') == True

def test_case8():
    assert reconhece('DCBA4321') == True

def test_case9():
    assert reconhece('A') == False

def test_case10():
    assert reconhece('1') == False

def test_case11():
    assert reconhece('') == False

def test_case12():
    assert reconhece('A0') == False

def test_case13():
    assert reconhece('E1') == False

def test_case14():
    assert reconhece('ABCDE1234') == False

def test_case15():
    assert reconhece('abc12') == False

def test_case16():
    assert reconhece('1A') == False

def test_case17():
    assert reconhece('ABCD') == False

def test_case18():
    assert reconhece('1234') == False

def test_case19():
    assert reconhece('A5') == False

def test_case20():
    assert reconhece('AB12') == True
