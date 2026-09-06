def test_case1():
    assert transforma([1, 2, 3, 4], lambda x: x ** 3) == [1, 8, 27, 64]

def test_case2():
    assert transforma([], lambda x: x + 1) == []

def test_case3():
    assert transforma([5], lambda x: x * 2) == [10]

def test_case4():
    assert transforma([1, 2, 3], lambda x: x ** 2) == [1, 4, 9]

def test_case5():
    assert transforma([2, 4, 6], lambda x: x // 2) == [1, 2, 3]

def test_case6():
    assert transforma([1, 1, 1], lambda x: x + 10) == [11, 11, 11]

def test_case7():
    assert transforma([1, 2, 3, 4, 5], lambda x: x * 2) == [2, 4, 6, 8, 10]

def test_case8():
    assert transforma([10, 20, 30], lambda x: x // 10) == [1, 2, 3]

def test_case9():
    result = transforma([1, 2, 3], lambda x: x * x)
    assert isinstance(result, list)

def test_case10():
    assert transforma([3, 5, 7], lambda x: x - 1) == [2, 4, 6]

def test_case11():
    assert transforma([1, 2, 3, 4, 5], lambda x: 0) == [0, 0, 0, 0, 0]

def test_case12():
    assert transforma([2, 3, 4], lambda x: x ** 2) == [4, 9, 16]

def test_case13():
    lst = [1, 2, 3]
    result = transforma(lst, lambda x: x * 3)
    assert result == [3, 6, 9]
    assert lst == [1, 2, 3]

def test_case14():
    assert transforma([1, 4, 9], lambda x: x ** 0.5) == [1.0, 2.0, 3.0]

def test_case15():
    assert transforma([-1, -2, -3], lambda x: abs(x)) == [1, 2, 3]

def test_case16():
    assert transforma([1, 2, 3, 4, 5], lambda x: x + 100) == [101, 102, 103, 104, 105]

def test_case17():
    assert transforma([5, 10, 15], lambda x: x % 7) == [5, 3, 1]

def test_case18():
    assert transforma([1], lambda x: x ** 10) == [1]

def test_case19():
    assert len(transforma([1, 2, 3, 4], lambda x: x)) == 4

def test_case20():
    assert transforma([0, 1, 2], lambda x: x * x) == [0, 1, 4]
