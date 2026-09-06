def test_case1():
    assert lposicoes([1, 2, 3, 4, 2, 2], 2) == [1, 4, 5]

def test_case2():
    assert lposicoes([], 1) == []

def test_case3():
    assert lposicoes([1, 2, 3], 5) == []

def test_case4():
    assert lposicoes([1, 1, 1], 1) == [0, 1, 2]

def test_case5():
    assert lposicoes([5, 3, 5, 5, 2], 5) == [0, 2, 3]

def test_case6():
    assert lposicoes([0, 1, 0, 1, 0], 0) == [0, 2, 4]

def test_case7():
    assert lposicoes([1, 2, 3], 1) == [0]

def test_case8():
    assert lposicoes([1, 2, 3], 3) == [2]

def test_case9():
    assert lposicoes([1, 2, 3], 2) == [1]

def test_case10():
    assert lposicoes([2, 2, 2, 2], 2) == [0, 1, 2, 3]

def test_case11():
    assert lposicoes([1, 2, 3, 4, 5], 6) == []

def test_case12():
    result = lposicoes([1, 2, 3], 2)
    assert isinstance(result, list)

def test_case13():
    assert lposicoes([7], 7) == [0]

def test_case14():
    assert lposicoes([7], 8) == []

def test_case15():
    assert lposicoes([1, 2, 1, 3, 1], 1) == [0, 2, 4]

def test_case16():
    assert lposicoes([3, 1, 4, 1, 5, 9, 2, 6], 1) == [1, 3]

def test_case17():
    assert lposicoes([0, 0, 0], 0) == [0, 1, 2]

def test_case18():
    assert lposicoes([1, 2, 3, 4, 5], 3) == [2]

def test_case19():
    assert lposicoes(['a', 'b', 'a', 'c', 'a'], 'a') == [0, 2, 4]

def test_case20():
    assert lposicoes([10, 20, 10, 30, 10], 10) == [0, 2, 4]
