def test_case1():
    assert maior([1]) == 1

def test_case2():
    assert maior([3, 1, 4, 1, 5, 9, 2, 6]) == 9

def test_case3():
    assert maior([-1, -2, -3]) == -1

def test_case4():
    assert maior([5, 5, 5]) == 5

def test_case5():
    assert maior([1, 2, 3, 4, 5]) == 5

def test_case6():
    assert maior([5, 4, 3, 2, 1]) == 5

def test_case7():
    assert maior([0]) == 0

def test_case8():
    assert maior([100]) == 100

def test_case9():
    assert maior([3, 3, 3, 3]) == 3

def test_case10():
    assert maior([1, 10, 2, 9, 3]) == 10

def test_case11():
    assert maior([-5, -3, -1]) == -1

def test_case12():
    result = maior([1, 2, 3])
    assert isinstance(result, int)

def test_case13():
    assert maior([7]) == 7

def test_case14():
    assert maior([2, 1]) == 2

def test_case15():
    assert maior([1, 2]) == 2

def test_case16():
    assert maior([0, 0, 1]) == 1

def test_case17():
    assert maior([99, 100, 1]) == 100

def test_case18():
    assert maior([5, 3, 8, 1]) == 8

def test_case19():
    assert maior([1, 1, 1, 2]) == 2

def test_case20():
    assert maior([-10, 0, 10]) == 10
