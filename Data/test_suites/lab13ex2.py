def test_case1():
    assert junta_ordenadas([], []) == []

def test_case2():
    assert junta_ordenadas([1], []) == [1]

def test_case3():
    assert junta_ordenadas([], [1]) == [1]

def test_case4():
    assert junta_ordenadas([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_case5():
    assert junta_ordenadas([2, 5, 90], [3, 5, 6, 12]) == [2, 3, 5, 5, 6, 12, 90]

def test_case6():
    assert junta_ordenadas([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]

def test_case7():
    assert junta_ordenadas([1, 1, 1], [2, 2, 2]) == [1, 1, 1, 2, 2, 2]

def test_case8():
    assert junta_ordenadas([5], [1, 2, 3]) == [1, 2, 3, 5]

def test_case9():
    assert junta_ordenadas([1, 2, 3], [5]) == [1, 2, 3, 5]

def test_case10():
    assert junta_ordenadas([1], [1]) == [1, 1]

def test_case11():
    assert junta_ordenadas([10], [1, 2, 3, 4]) == [1, 2, 3, 4, 10]

def test_case12():
    assert junta_ordenadas([1, 2, 3, 4], [10]) == [1, 2, 3, 4, 10]

def test_case13():
    assert junta_ordenadas([-3, -1, 0, 2], [-2, 1, 3]) == [-3, -2, -1, 0, 1, 2, 3]

def test_case14():
    assert junta_ordenadas([1, 3, 5, 7], [2, 4, 6, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_case15():
    assert junta_ordenadas([2, 4, 6, 8], [1, 3, 5, 7]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_case16():
    assert junta_ordenadas([1], [2]) == [1, 2]

def test_case17():
    assert junta_ordenadas([2], [1]) == [1, 2]

def test_case18():
    assert junta_ordenadas([0, 0], [0, 0]) == [0, 0, 0, 0]

def test_case19():
    result = junta_ordenadas([1, 2], [3, 4])
    assert isinstance(result, list)

def test_case20():
    assert junta_ordenadas([1, 2, 5, 8, 10], [3, 6, 7, 9]) == [1, 2, 3, 5, 6, 7, 8, 9, 10]
