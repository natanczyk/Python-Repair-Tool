def test_case1():
    assert inverte([]) == []

def test_case2():
    assert inverte([1]) == [1]

def test_case3():
    assert inverte([1, 2, 3]) == [3, 2, 1]

def test_case4():
    assert inverte([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

def test_case5():
    assert inverte([3, 2, 1]) == [1, 2, 3]

def test_case6():
    assert inverte(['a', 'b', 'c']) == ['c', 'b', 'a']

def test_case7():
    assert inverte([1, 1, 1]) == [1, 1, 1]

def test_case8():
    assert inverte([5, 4]) == [4, 5]

def test_case9():
    assert inverte([1, 2]) == [2, 1]

def test_case10():
    assert inverte([10, 20, 30, 40]) == [40, 30, 20, 10]

def test_case11():
    result = inverte([1, 2, 3])
    assert isinstance(result, list)

def test_case12():
    original = [1, 2, 3]
    result = inverte(original)
    assert original == [1, 2, 3]

def test_case13():
    assert inverte([0]) == [0]

def test_case14():
    assert inverte([-1, -2, -3]) == [-3, -2, -1]

def test_case15():
    assert inverte([1, 2, 3, 4]) == [4, 3, 2, 1]

def test_case16():
    assert inverte(['x']) == ['x']

def test_case17():
    assert inverte([True, False]) == [False, True]

def test_case18():
    assert inverte([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]

def test_case19():
    assert inverte([7, 3, 9, 1]) == [1, 9, 3, 7]

def test_case20():
    assert inverte([100, 200]) == [200, 100]
