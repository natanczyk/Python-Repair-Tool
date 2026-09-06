def test_case1():
    assert calc_soma(0, 0) == 1.0

def test_case2():
    assert calc_soma(0, 5) == 1.0

def test_case3():
    assert calc_soma(1, 0) == 1.0

def test_case4():
    assert calc_soma(1, 1) == 2.0

def test_case5():
    assert calc_soma(1, 2) == 2.5

def test_case6():
    assert calc_soma(2, 0) == 1.0

def test_case7():
    assert calc_soma(2, 1) == 3.0

def test_case8():
    assert calc_soma(2, 2) == 5.0

def test_case9():
    assert calc_soma(3, 0) == 1.0

def test_case10():
    assert calc_soma(3, 1) == 4.0

def test_case11():
    assert calc_soma(3, 2) == 8.5

def test_case12():
    result = calc_soma(1, 1)
    assert isinstance(result, (int, float))

def test_case13():
    assert abs(calc_soma(1, 3) - (1 + 1 + 0.5 + 1/6)) < 1e-9

def test_case14():
    assert abs(calc_soma(2, 3) - (1 + 2 + 2 + 4/6)) < 1e-9

def test_case15():
    assert calc_soma(1, 0) < calc_soma(1, 1)

def test_case16():
    assert calc_soma(2, 0) < calc_soma(2, 2)

def test_case17():
    assert abs(calc_soma(1, 4) - (1 + 1 + 0.5 + 1/6 + 1/24)) < 1e-9

def test_case18():
    assert calc_soma(0, 3) == 1.0

def test_case19():
    assert calc_soma(1, 2) < calc_soma(1, 3)

def test_case20():
    assert calc_soma(2, 4) == 7.0
