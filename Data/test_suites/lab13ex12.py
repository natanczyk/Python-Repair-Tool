def test_case1():
    assert sufixo([], []) == True

def test_case2():
    assert sufixo([], [1, 2, 3]) == True

def test_case3():
    assert sufixo([1], [1]) == True

def test_case4():
    assert sufixo([4, 5, 6], [1, 2, 3, 4, 5, 6]) == True

def test_case5():
    assert sufixo([1, 2], [1, 2, 3]) == False

def test_case6():
    assert sufixo([1, 2, 3], [1, 2]) == False

def test_case7():
    assert sufixo([1, 2, 3], [1, 2, 3]) == True

def test_case8():
    assert sufixo([3], [1, 2, 3]) == True

def test_case9():
    assert sufixo([2, 3], [1, 2, 3]) == True

def test_case10():
    assert sufixo([1, 3], [1, 2, 3]) == False

def test_case11():
    assert sufixo([1, 2, 3], [4, 5, 6]) == False

def test_case12():
    result = sufixo([1], [1, 2])
    assert isinstance(result, bool)

def test_case13():
    assert sufixo([5, 6], [1, 2, 3, 4, 5, 6]) == True

def test_case14():
    assert sufixo([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) == True

def test_case15():
    assert sufixo([6], [1, 2, 3, 4, 5, 6]) == True

def test_case16():
    assert sufixo([1], [1, 2, 3, 4, 5, 6]) == False

def test_case17():
    assert sufixo([3, 4], [1, 2, 3, 4, 5, 6]) == False

def test_case18():
    assert sufixo(['b', 'c'], ['a', 'b', 'c']) == True

def test_case19():
    assert sufixo(['a', 'b'], ['a', 'b', 'c']) == False

def test_case20():
    assert sufixo([1, 2, 3, 4, 5, 7], [1, 2, 3, 4, 5, 6]) == False
