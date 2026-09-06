def test_case1():
    assert subtrai([], [1, 2]) == []

def test_case2():
    assert subtrai([1, 2, 3], []) == [1, 2, 3]

def test_case3():
    assert subtrai([2, 3, 4, 5, 3], [2, 3]) == [4, 5]

def test_case4():
    assert subtrai([1, 2, 3, 4, 5], [2, 4]) == [1, 3, 5]

def test_case5():
    assert subtrai([1, 1, 1, 1], [1]) == []

def test_case6():
    assert subtrai([1, 2, 3], [4, 5]) == [1, 2, 3]

def test_case7():
    assert subtrai([1, 2, 3], [1, 2, 3]) == []

def test_case8():
    assert subtrai([5, 3, 5, 5, 2], [5]) == [3, 2]

def test_case9():
    assert subtrai([], []) == []

def test_case10():
    assert subtrai([1, 2, 3, 4, 5], [1, 5]) == [2, 3, 4]

def test_case11():
    assert subtrai([1, 2, 3], [2]) == [1, 3]

def test_case12():
    result = subtrai([1, 2, 3], [2])
    assert isinstance(result, list)

def test_case13():
    assert subtrai([1, 2, 3, 2, 1], [1, 2]) == [3]

def test_case14():
    assert subtrai([10, 20, 30], [20]) == [10, 30]

def test_case15():
    assert subtrai([1, 2, 3, 4, 5, 6], [2, 4, 6]) == [1, 3, 5]

def test_case16():
    assert subtrai([0, 0, 1, 0], [0]) == [1]

def test_case17():
    assert subtrai([1, 2, 3, 4], [5, 6, 7]) == [1, 2, 3, 4]

def test_case18():
    assert subtrai([3, 3, 3], [3, 3]) == []

def test_case19():
    assert subtrai([1, 2, 3, 4, 5], [3]) == [1, 2, 4, 5]

def test_case20():
    assert subtrai(['a', 'b', 'c', 'b'], ['b']) == ['a', 'c']
