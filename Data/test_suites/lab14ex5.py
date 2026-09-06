def test_case1():
    assert espelho(391) == 193

def test_case2():
    assert espelho(45679) == 97654

def test_case3():
    assert espelho(1230000) == 321

def test_case4():
    assert espelho(1) == 1

def test_case5():
    assert espelho(9) == 9

def test_case6():
    assert espelho(10) == 1

def test_case7():
    assert espelho(100) == 1

def test_case8():
    assert espelho(123) == 321

def test_case9():
    assert espelho(1234) == 4321

def test_case10():
    assert espelho(12321) == 12321

def test_case11():
    assert espelho(9876) == 6789

def test_case12():
    result = espelho(123)
    assert isinstance(result, int)

def test_case13():
    assert espelho(5000) == 5

def test_case14():
    assert espelho(11) == 11

def test_case15():
    assert espelho(23) == 32

def test_case16():
    assert espelho(200) == 2

def test_case17():
    assert espelho(1001) == 1001

def test_case18():
    assert espelho(54321) == 12345

def test_case19():
    assert espelho(1000000) == 1

def test_case20():
    assert espelho(1234567) == 7654321
