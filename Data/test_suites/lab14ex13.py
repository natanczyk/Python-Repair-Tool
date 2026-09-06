def test_case1():
    assert listas_iguais([], []) == True

def test_case2():
    assert listas_iguais([1, 2, 3], [1, 2, 3]) == True

def test_case3():
    assert listas_iguais([1, 2, 3], [3, 2, 1]) == False

def test_case4():
    assert listas_iguais([1, 2, 3], [1, 2]) == False

def test_case5():
    assert listas_iguais([1, 2], [1, 2, 3]) == False

def test_case6():
    assert listas_iguais([1], [1]) == True

def test_case7():
    assert listas_iguais([1], [2]) == False

def test_case8():
    assert listas_iguais([0, 0, 0], [0, 0, 0]) == True

def test_case9():
    assert listas_iguais([1, 1, 1], [1, 1, 2]) == False

def test_case10():
    result = listas_iguais([], [])
    assert isinstance(result, bool)

def test_case11():
    assert listas_iguais([5], []) == False

def test_case12():
    assert listas_iguais([], [5]) == False

def test_case13():
    assert listas_iguais([1, 2, 3, 4], [1, 2, 3, 4]) == True

def test_case14():
    assert listas_iguais([1, 2, 3, 4], [1, 2, 3, 5]) == False

def test_case15():
    assert listas_iguais([1, 2, 3], [1, 2, 4]) == False

def test_case16():
    assert listas_iguais(['a', 'b'], ['a', 'b']) == True

def test_case17():
    assert listas_iguais(['a', 'b'], ['a', 'c']) == False

def test_case18():
    assert listas_iguais([1, 2], [2, 1]) == False

def test_case19():
    assert listas_iguais([10, 20, 30], [10, 20, 30]) == True

def test_case20():
    assert listas_iguais([10, 20, 30], [10, 20]) == False
