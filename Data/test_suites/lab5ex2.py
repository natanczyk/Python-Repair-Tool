def test_case1():
    assert horas_dias(48) == 2.0

def test_case2():
    assert horas_dias(10) == 10 / 24

def test_case3():
    assert horas_dias(24) == 1.0

def test_case4():
    assert horas_dias(0) == 0.0

def test_case5():
    assert horas_dias(12) == 0.5

def test_case6():
    assert horas_dias(1) == 1 / 24

def test_case7():
    assert horas_dias(36) == 1.5

def test_case8():
    assert horas_dias(72) == 3.0

def test_case9():
    assert horas_dias(6) == 0.25

def test_case10():
    assert horas_dias(168) == 7.0

def test_case11():
    assert horas_dias(240) == 10.0

def test_case12():
    assert horas_dias(3) == 3 / 24

def test_case13():
    assert horas_dias(96) == 4.0

def test_case14():
    assert horas_dias(16) == 16 / 24

def test_case15():
    assert horas_dias(8) == 8 / 24

def test_case16():
    assert horas_dias(100) == 100 / 24

def test_case17():
    assert horas_dias(15) == 15 / 24

def test_case18():
    assert horas_dias(120) == 5.0

def test_case19():
    assert horas_dias(144) == 6.0

def test_case20():
    assert horas_dias(2) == 2 / 24
