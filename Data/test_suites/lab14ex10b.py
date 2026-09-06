def test_case1():
    assert perfeitos_entre(1, 5) == []

def test_case2():
    assert perfeitos_entre(6, 6) == [6]

def test_case3():
    assert perfeitos_entre(6, 30) == [6, 28]

def test_case4():
    assert perfeitos_entre(1, 10) == [6]

def test_case5():
    assert perfeitos_entre(1, 28) == [6, 28]

def test_case6():
    assert perfeitos_entre(28, 28) == [28]

def test_case7():
    assert perfeitos_entre(29, 100) == []

def test_case8():
    assert perfeitos_entre(7, 27) == []

def test_case9():
    assert perfeitos_entre(7, 28) == [28]

def test_case10():
    result = perfeitos_entre(1, 10)
    assert isinstance(result, list)

def test_case11():
    assert perfeitos_entre(1, 496) == [6, 28, 496]

def test_case12():
    assert perfeitos_entre(5, 6) == [6]

def test_case13():
    assert perfeitos_entre(1, 1) == []

def test_case14():
    assert perfeitos_entre(100, 495) == []

def test_case15():
    assert perfeitos_entre(496, 496) == [496]

def test_case16():
    assert len(perfeitos_entre(1, 30)) == 2

def test_case17():
    assert 6 in perfeitos_entre(1, 100)

def test_case18():
    assert 28 not in perfeitos_entre(1, 27)

def test_case19():
    assert perfeitos_entre(6, 28) == [6, 28]

def test_case20():
    assert perfeitos_entre(27, 30) == [28]
