def test_case1():
    assert acumula([1, 2, 3, 4], lambda x, y: x + y) == 10

def test_case2():
    assert acumula([1, 2, 3, 4], lambda x, y: x * y) == 24

def test_case3():
    assert acumula([5], lambda x, y: x + y) == 5

def test_case4():
    assert acumula([2, 2, 2, 2], lambda x, y: x * y) == 16

def test_case5():
    assert acumula([1, 2, 3, 4, 5], lambda x, y: x + y) == 15

def test_case6():
    assert acumula([10], lambda x, y: x * y) == 10

def test_case7():
    assert acumula([1, 2], lambda x, y: x + y) == 3

def test_case8():
    assert acumula([1, 2], lambda x, y: x * y) == 2

def test_case9():
    assert acumula([3, 3, 3], lambda x, y: x + y) == 9

def test_case10():
    assert acumula([1, 1, 1, 1, 1], lambda x, y: x * y) == 1

def test_case11():
    assert acumula([2, 3, 4], lambda x, y: x * y) == 24

def test_case12():
    assert acumula([10, 20, 30], lambda x, y: x + y) == 60

def test_case13():
    result = acumula([1, 2, 3], lambda x, y: x + y)
    assert isinstance(result, int)

def test_case14():
    assert acumula([5, 5], lambda x, y: x + y) == 10

def test_case15():
    assert acumula([5, 5], lambda x, y: x * y) == 25

def test_case16():
    assert acumula([100], lambda x, y: x + y) == 100

def test_case17():
    assert acumula([1, 2, 3, 4, 5, 6], lambda x, y: x + y) == 21

def test_case18():
    assert acumula([2, 4, 8], lambda x, y: x * y) == 64

def test_case19():
    assert acumula([0, 1, 2, 3], lambda x, y: x + y) == 6

def test_case20():
    assert acumula([1, 10, 100], lambda x, y: x + y) == 111
