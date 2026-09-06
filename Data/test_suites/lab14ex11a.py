def test_case1():
    assert fib(0) == 1

def test_case2():
    assert fib(1) == 1

def test_case3():
    assert fib(2) == 2

def test_case4():
    assert fib(3) == 3

def test_case5():
    assert fib(4) == 5

def test_case6():
    assert fib(5) == 8

def test_case7():
    assert fib(6) == 13

def test_case8():
    assert fib(7) == 21

def test_case9():
    assert fib(8) == 34

def test_case10():
    assert fib(9) == 55

def test_case11():
    assert fib(10) == 89

def test_case12():
    result = fib(5)
    assert isinstance(result, int)

def test_case13():
    assert fib(11) == 144

def test_case14():
    assert fib(12) == 233

def test_case15():
    assert fib(15) == 987

def test_case16():
    assert fib(5) == fib(4) + fib(3)

def test_case17():
    assert fib(10) == fib(9) + fib(8)

def test_case18():
    assert fib(0) > 0

def test_case19():
    assert fib(1) == fib(0)

def test_case20():
    assert fib(20) == 10946
