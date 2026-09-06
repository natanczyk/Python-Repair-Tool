def test_case1():
    assert prim_alg(123) == 1

def test_case2():
    assert prim_alg(9) == 9

def test_case3():
    assert prim_alg(1000) == 1

def test_case4():
    assert prim_alg(5678) == 5

def test_case5():
    assert prim_alg(100) == 1

def test_case6():
    assert prim_alg(999) == 9

def test_case7():
    assert prim_alg(1) == 1

def test_case8():
    assert prim_alg(5) == 5

def test_case9():
    assert prim_alg(12345) == 1

def test_case10():
    assert prim_alg(99999) == 9

def test_case11():
    assert prim_alg(30) == 3

def test_case12():
    assert prim_alg(500) == 5

def test_case13():
    result = prim_alg(123)
    assert isinstance(result, int)

def test_case14():
    assert prim_alg(7654321) == 7

def test_case15():
    assert prim_alg(2000) == 2

def test_case16():
    assert prim_alg(4321) == 4

def test_case17():
    assert prim_alg(6) == 6

def test_case18():
    assert prim_alg(80000) == 8

def test_case19():
    assert prim_alg(31415) == 3

def test_case20():
    assert prim_alg(10) == 1
