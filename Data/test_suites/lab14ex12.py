def test_case1():
    assert conta_ord([]) == 0

def test_case2():
    assert conta_ord([[2, 2, 3, 0], [1, 2, 5, 4], [2, 4, 4]]) == 1

def test_case3():
    assert conta_ord([[1, 2, 3], [4, 5, 6]]) == 2

def test_case4():
    assert conta_ord([[3, 2, 1]]) == 0

def test_case5():
    assert conta_ord([[1, 2, 3]]) == 1

def test_case6():
    assert conta_ord([[1], [2], [3]]) == 3

def test_case7():
    assert conta_ord([[]]) == 1

def test_case8():
    assert conta_ord([[1, 1, 1]]) == 1

def test_case9():
    assert conta_ord([[1, 1, 2], [3, 2, 1]]) == 1

def test_case10():
    assert conta_ord([[1], [], [2, 3]]) == 3

def test_case11():
    result = conta_ord([])
    assert isinstance(result, int)

def test_case12():
    assert conta_ord([[5, 4, 3, 2, 1]]) == 0

def test_case13():
    assert conta_ord([[1, 2, 3, 4, 5]]) == 1

def test_case14():
    assert conta_ord([[0, 0, 0, 0]]) == 1

def test_case15():
    assert conta_ord([[2, 1], [1, 2], [2, 3]]) == 2

def test_case16():
    assert conta_ord([[1, 2], [2, 1], [3, 4]]) == 2

def test_case17():
    assert conta_ord([[1, 2, 3], [3, 2, 1], [2, 2, 2]]) == 2

def test_case18():
    assert conta_ord([[10, 20, 30], [30, 20, 10]]) == 1

def test_case19():
    assert conta_ord([[1, 1], [2, 2], [3, 3]]) == 3

def test_case20():
    assert conta_ord([[1, 2, 2, 3], [3, 2, 2, 1]]) == 1
