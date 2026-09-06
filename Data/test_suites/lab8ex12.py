def test_case1():
    assert reconhece([1, 2, 3], [2, 1, 2, 3, 4, 5]) == True

def test_case2():
    assert reconhece([4, 3, 4], [2, 1, 4, 2, 3, 4, 5]) == False

def test_case3():
    assert reconhece([5, 2, 7], [5, 2, 7]) == True

def test_case4():
    assert reconhece([9, 4], [3, 2, 4, 2, 9, 4]) == True

def test_case5():
    assert reconhece([7, 4, 3], [7, 4, 7, 4, 3, 7, 2, 7]) == True

def test_case6():
    assert reconhece([], [1, 2, 3]) == True

def test_case7():
    assert reconhece([1, 2], []) == False

def test_case8():
    assert reconhece([1, 2, 3], [1, 2]) == False

def test_case9():
    assert reconhece([1], [1, 2, 3]) == True

def test_case10():
    assert reconhece([3], [1, 2, 3]) == True

def test_case11():
    assert reconhece([1, 2], [3, 1, 2]) == True

def test_case12():
    assert reconhece([1, 2], [1, 3, 2]) == False

def test_case13():
    assert reconhece([1, 2, 3], [1, 2, 4]) == False

def test_case14():
    assert reconhece([2, 1], [1, 2]) == False

def test_case15():
    assert reconhece([1, 1], [1, 1, 2]) == True

def test_case16():
    assert reconhece([1, 1, 1], [1, 1, 0, 1, 1, 1]) == True

def test_case17():
    assert reconhece([2, 3], [1, 2, 3, 4]) == True

def test_case18():
    assert reconhece([4, 5], [1, 2, 3, 4]) == False

def test_case19():
    assert reconhece([1, 2, 3], [1, 2, 3]) == True

def test_case20():
    assert reconhece([5], [1, 2, 3, 4]) == False
