def test_case1():
    assert filtra_pares(5467829) == 4682

def test_case2():
    assert filtra_pares(2) == 2

def test_case3():
    assert filtra_pares(1) == 0

def test_case4():
    assert filtra_pares(135) == 0

def test_case5():
    assert filtra_pares(246) == 246

def test_case6():
    assert filtra_pares(12) == 2

def test_case7():
    assert filtra_pares(20) == 20

def test_case8():
    assert filtra_pares(42) == 42

def test_case9():
    assert filtra_pares(1234) == 24

def test_case10():
    assert filtra_pares(9999) == 0

def test_case11():
    assert filtra_pares(12345678) == 2468

def test_case12():
    assert filtra_pares(468) == 468

def test_case13():
    assert filtra_pares(555) == 0

def test_case14():
    assert filtra_pares(80) == 80

def test_case15():
    result = filtra_pares(5467829)
    assert isinstance(result, int)

def test_case16():
    assert filtra_pares(246802) == 246802

def test_case17():
    assert filtra_pares(3) == 0

def test_case18():
    assert filtra_pares(4) == 4

def test_case19():
    assert filtra_pares(13579) == 0

def test_case20():
    assert filtra_pares(2048) == 2048
