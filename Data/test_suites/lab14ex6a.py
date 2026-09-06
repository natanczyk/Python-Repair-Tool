def test_case1():
    assert g(0) == 0

def test_case2():
    assert g(1) == 1

def test_case3():
    assert g(2) == 1

def test_case4():
    assert g(3) == 2

def test_case5():
    assert g(4) == 3

def test_case6():
    assert g(5) == 3

def test_case7():
    assert g(6) == 4

def test_case8():
    assert g(7) == 4

def test_case9():
    assert g(8) == 5

def test_case10():
    assert g(9) == 6

def test_case11():
    assert g(10) == 6

def test_case12():
    result = g(5)
    assert isinstance(result, int)

def test_case13():
    assert g(11) == 7

def test_case14():
    assert g(12) == 8

def test_case15():
    assert g(13) == 8

def test_case16():
    assert g(14) == 9

def test_case17():
    assert g(15) == 9

def test_case18():
    assert g(0) >= 0

def test_case19():
    assert g(20) == 12

def test_case20():
    assert g(25) == 16
