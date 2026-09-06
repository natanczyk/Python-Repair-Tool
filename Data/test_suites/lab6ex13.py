def test_case1():
    assert permutacao((1, 2, 3), (1, 2, 3)) == True

def test_case2():
    assert permutacao((1, 2, 3), (2, 3, 1)) == True

def test_case3():
    assert permutacao((1, 1, 1, 2, 3), (1, 2, 3)) == False

def test_case4():
    assert permutacao((1, 2, 3), (1, 2, 3, 4)) == False

def test_case5():
    assert permutacao((), ()) == True

def test_case6():
    assert permutacao((1,), (2,)) == False

def test_case7():
    assert permutacao((1, 2), (2, 1)) == True

def test_case8():
    assert permutacao((1, 1), (1, 2)) == False

def test_case9():
    assert permutacao((3, 2, 1), (1, 2, 3)) == True

def test_case10():
    assert permutacao((1, 2, 3), (4, 5, 6)) == False

def test_case11():
    assert permutacao((1,), (1,)) == True

def test_case12():
    assert permutacao((1, 2, 2, 3), (3, 2, 1, 2)) == True

def test_case13():
    assert permutacao((1, 2, 3), (1, 2, 2)) == False

def test_case14():
    assert permutacao((1, 2, 3), (3, 1, 2)) == True

def test_case15():
    assert permutacao((1, 1, 2), (1, 2, 2)) == False

def test_case16():
    assert permutacao((5, 5, 5), (5, 5, 5)) == True

def test_case17():
    assert permutacao((1, 2), (1, 2, 3)) == False

def test_case18():
    assert permutacao((4, 3, 2, 1), (1, 2, 3, 4)) == True

def test_case19():
    assert permutacao((1,), ()) == False

def test_case20():
    assert permutacao((2, 2, 1), (1, 2, 2)) == True
