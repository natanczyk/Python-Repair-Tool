def test_case1():
    assert apaga1((1, 2, 4, 2, 1), 2) == (1, 4, 2, 1)

def test_case2():
    assert apaga1((1, 2, 3), 4) == (1, 2, 3)

def test_case3():
    assert apaga1((1,), 1) == ()

def test_case4():
    assert apaga1((), 1) == ()

def test_case5():
    assert apaga1((1, 1, 1), 1) == (1, 1)

def test_case6():
    assert apaga1((2, 1, 3), 2) == (1, 3)

def test_case7():
    assert apaga1((1, 2, 3, 1, 2, 3), 2) == (1, 3, 1, 2, 3)

def test_case8():
    assert apaga1((5, 5, 5), 5) == (5, 5)

def test_case9():
    assert apaga1((1, 2, 3), 1) == (2, 3)

def test_case10():
    assert apaga1((1, 2, 3), 3) == (1, 2)

def test_case11():
    assert apaga1((3, 1, 2), 3) == (1, 2)

def test_case12():
    assert apaga1((1, 2, 3, 4), 2) == (1, 3, 4)

def test_case13():
    assert apaga1((1,), 2) == (1,)

def test_case14():
    assert apaga1((0, 0, 0), 0) == (0, 0)

def test_case15():
    assert apaga1((1, 2, 1, 2), 1) == (2, 1, 2)

def test_case16():
    assert apaga1((10, 20, 30, 20), 20) == (10, 30, 20)

def test_case17():
    assert apaga1((1, 2, 3), 2) == (1, 3)

def test_case18():
    assert apaga1((5,), 5) == ()

def test_case19():
    assert apaga1((1, 3, 5, 3, 1), 3) == (1, 5, 3, 1)

def test_case20():
    assert apaga1((2, 2), 2) == (2,)
