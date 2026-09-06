def test_case1():
    assert factorial(5) == 120

def test_case2():
    assert factorial(0) == 1

def test_case3():
    assert factorial(1) == 1

def test_case4():
    assert factorial(4) == 24

def test_case5():
    assert factorial(3) == 6

def test_case6():
    assert factorial(6) == 720

def test_case7():
    assert factorial(7) == 5040

def test_case8():
    assert factorial(10) == 3628800

def test_case9():
    assert factorial(2) == 2

def test_case10():
    assert factorial(8) == 40320

def test_case11():
    assert factorial(9) == 362880

def test_case12():
    result = factorial(5)
    assert isinstance(result, int)

def test_case13():
    assert factorial(1) == factorial(0)

def test_case14():
    assert factorial(5) == 5 * factorial(4)

def test_case15():
    assert factorial(6) == 6 * factorial(5)

def test_case16():
    assert factorial(4) == 4 * factorial(3)

def test_case17():
    assert factorial(3) == 3 * factorial(2)

def test_case18():
    assert factorial(2) == 2 * factorial(1)

def test_case19():
    assert factorial(12) == 479001600

def test_case20():
    assert factorial(11) == 39916800
