def test_case1():
    assert pertence([], 5) == False

def test_case2():
    assert pertence([1, 2, 3], 2) == True

def test_case3():
    assert pertence([1, 2, 3], 5) == False

def test_case4():
    assert pertence([1, 2, 3], 1) == True

def test_case5():
    assert pertence([1, 2, 3], 3) == True

def test_case6():
    assert pertence([1, 2, 3], 4) == False

def test_case7():
    assert pertence([5], 5) == True

def test_case8():
    assert pertence([5], 4) == False

def test_case9():
    assert pertence([0, 1, 2], 0) == True

def test_case10():
    assert pertence([0, 1, 2], 3) == False

def test_case11():
    assert pertence(['a', 'b', 'c'], 'b') == True

def test_case12():
    assert pertence(['a', 'b', 'c'], 'd') == False

def test_case13():
    assert pertence([1, 1, 1], 1) == True

def test_case14():
    assert pertence([1, 1, 1], 2) == False

def test_case15():
    assert pertence([0.1, 0.2, 0.8], 0.7 + 0.1) == False

def test_case16():
    assert pertence([0.1, 0.2, 0.8], 0.8) == True

def test_case17():
    result = pertence([1, 2, 3], 2)
    assert isinstance(result, bool)

def test_case18():
    assert pertence([-1, -2, -3], -2) == True

def test_case19():
    assert pertence([-1, -2, -3], 0) == False

def test_case20():
    assert pertence([10, 20, 30, 40, 50], 30) == True
