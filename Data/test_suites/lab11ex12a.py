def test_case1():
    assert nest(lambda x: x + 1, 0, 5) == 5

def test_case2():
    assert nest(lambda x: x * 2, 1, 3) == 8

def test_case3():
    assert nest(lambda x: x + 1, 10, 0) == 10

def test_case4():
    assert nest(lambda x: x ** 2, 2, 3) == 256

def test_case5():
    assert nest(lambda x: x + 1, 0, 10) == 10

def test_case6():
    assert nest(lambda x: x * 3, 1, 4) == 81

def test_case7():
    assert nest(lambda x: x + 2, 0, 5) == 10

def test_case8():
    assert nest(lambda x: x * x, 2, 2) == 16

def test_case9():
    assert nest(lambda x: x - 1, 10, 3) == 7

def test_case10():
    assert nest(lambda x: x + 1, 0, 1) == 1

def test_case11():
    assert nest(lambda x: x + 1, 5, 5) == 10

def test_case12():
    assert nest(lambda x: x * 2, 1, 0) == 1

def test_case13():
    assert nest(lambda x: x * 2, 2, 4) == 32

def test_case14():
    assert nest(lambda x: x + 1, 0, 100) == 100

def test_case15():
    assert nest(lambda x: x * 10, 1, 3) == 1000

def test_case16():
    assert nest(lambda x: -x, 1, 2) == 1

def test_case17():
    assert nest(lambda x: x + 0, 42, 5) == 42

def test_case18():
    assert nest(lambda x: x + 1, 99, 1) == 100

def test_case19():
    result = nest(lambda x: x + 1, 0, 5)
    assert isinstance(result, int)

def test_case20():
    assert nest(lambda x: x * 2, 3, 5) == 96
