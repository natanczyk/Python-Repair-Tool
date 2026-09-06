def test_case1():
    assert filtra([1, 2, 3, 4, 5], lambda x: x % 2 == 0) == [2, 4]

def test_case2():
    assert filtra([], lambda x: x % 2 == 0) == []

def test_case3():
    assert filtra([1, 3, 5], lambda x: x % 2 == 0) == []

def test_case4():
    assert filtra([2, 4, 6], lambda x: x % 2 == 0) == [2, 4, 6]

def test_case5():
    assert filtra([1, 2, 3], lambda x: x > 1) == [2, 3]

def test_case6():
    assert filtra([1, 2, 3], lambda x: x < 0) == []

def test_case7():
    assert filtra([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5]

def test_case8():
    assert filtra([10, 20, 30], lambda x: x > 15) == [20, 30]

def test_case9():
    assert filtra([5], lambda x: x > 3) == [5]

def test_case10():
    assert filtra([5], lambda x: x > 10) == []

def test_case11():
    assert filtra([1, 2, 3, 4, 5, 6], lambda x: x % 3 == 0) == [3, 6]

def test_case12():
    result = filtra([1, 2, 3], lambda x: x > 0)
    assert isinstance(result, list)

def test_case13():
    assert filtra([1, 1, 1, 2, 2], lambda x: x == 1) == [1, 1, 1]

def test_case14():
    assert filtra([10, 5, 8, 3, 7], lambda x: x >= 7) == [10, 8, 7]

def test_case15():
    lst = [1, 2, 3, 4, 5]
    result = filtra(lst, lambda x: x % 2 == 0)
    assert result == [2, 4]
    assert lst == [1, 2, 3, 4, 5]

def test_case16():
    assert filtra([1, 2, 3, 4], lambda x: True) == [1, 2, 3, 4]

def test_case17():
    assert filtra([1, 2, 3, 4], lambda x: False) == []

def test_case18():
    assert filtra([-3, -2, -1, 0, 1, 2], lambda x: x < 0) == [-3, -2, -1]

def test_case19():
    assert filtra([100, 200, 300], lambda x: x == 200) == [200]

def test_case20():
    assert filtra([2, 4, 6, 8], lambda x: x > 4) == [6, 8]
