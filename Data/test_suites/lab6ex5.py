def test_case1():
    assert algarismos_pares(6643399766641) == 6646664

def test_case2():
    assert algarismos_pares(1234) == 24

def test_case3():
    assert algarismos_pares(2468) == 2468

def test_case4():
    assert algarismos_pares(100) == 0

def test_case5():
    assert algarismos_pares(248) == 248

def test_case6():
    assert algarismos_pares(12) == 2

def test_case7():
    assert algarismos_pares(200) == 200

def test_case8():
    assert algarismos_pares(2) == 2

def test_case9():
    assert algarismos_pares(8) == 8

def test_case10():
    assert algarismos_pares(20) == 20

def test_case11():
    assert algarismos_pares(246) == 246

def test_case12():
    assert algarismos_pares(1246) == 246

def test_case13():
    assert algarismos_pares(1020) == 20

def test_case14():
    assert algarismos_pares(3456) == 456 - 400 + 400

def test_case15():
    assert algarismos_pares(123456) == 246

def test_case16():
    assert algarismos_pares(1000) == 0

def test_case17():
    assert algarismos_pares(2000) == 2000

def test_case18():
    assert algarismos_pares(6) == 6

def test_case19():
    assert algarismos_pares(400) == 400

def test_case20():
    assert algarismos_pares(12345678) == 2468
