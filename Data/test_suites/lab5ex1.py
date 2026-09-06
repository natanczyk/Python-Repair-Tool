def test_case1():
    assert cinco(5) == True

def test_case2():
    assert cinco(0) == False

def test_case3():
    assert cinco(-5) == False

def test_case4():
    assert cinco(10) == False

def test_case5():
    assert cinco(5.0) == True

def test_case6():
    assert cinco(4.999) == False

def test_case7():
    assert cinco(6) == False

def test_case8():
    assert cinco(1) == False

def test_case9():
    assert cinco(100) == False

def test_case10():
    assert cinco(-100) == False

def test_case11():
    assert cinco(4) == False

def test_case12():
    assert cinco(3) == False

def test_case13():
    assert cinco(7) == False

def test_case14():
    assert cinco(2) == False

def test_case15():
    assert cinco(55) == False

def test_case16():
    assert cinco(-1) == False

def test_case17():
    assert cinco(50) == False

def test_case18():
    assert cinco(5) is True

def test_case19():
    assert cinco(0) is False

def test_case20():
    assert cinco(999) == False
