def test_case1():
    assert duplicar(100, 0.03) == 24

def test_case2():
    assert duplicar(100, 0.07) == 11

def test_case3():
    assert duplicar(100, 0.10) == 8

def test_case4():
    assert duplicar(100, 0.05) == 15

def test_case5():
    assert duplicar(100, 0.12) == 7

def test_case6():
    assert duplicar(100, 0.20) == 4

def test_case7():
    assert duplicar(100, 0.50) == 2

def test_case8():
    assert duplicar(100, 0.01) == 70

def test_case9():
    assert duplicar(1000, 0.03) == 24

def test_case10():
    assert duplicar(500, 0.07) == 11

def test_case11():
    assert duplicar(200, 0.10) == 8

def test_case12():
    assert duplicar(1, 0.05) == 15

def test_case13():
    assert duplicar(9999, 0.12) == 7

def test_case14():
    assert duplicar(50, 0.20) == 4

def test_case15():
    assert duplicar(250, 0.50) == 2

def test_case16():
    assert duplicar(100, 0.03) > 0

def test_case17():
    assert isinstance(duplicar(100, 0.03), int)

def test_case18():
    assert duplicar(100, 0.10) < duplicar(100, 0.03)

def test_case19():
    assert duplicar(100, 0.07) < duplicar(100, 0.05)

def test_case20():
    assert duplicar(100, 0.20) < duplicar(100, 0.10)
