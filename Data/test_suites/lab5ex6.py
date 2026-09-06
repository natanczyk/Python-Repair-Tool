import pytest

def test_case1():
    assert dias_mes('jan', 2017) == 31

def test_case2():
    assert dias_mes('feb', 2016) == 29

def test_case3():
    assert dias_mes('feb', 2017) == 28

def test_case4():
    assert dias_mes('mar', 2017) == 31

def test_case5():
    assert dias_mes('apr', 2017) == 30

def test_case6():
    assert dias_mes('may', 2017) == 31

def test_case7():
    assert dias_mes('jun', 2017) == 30

def test_case8():
    assert dias_mes('jul', 2017) == 31

def test_case9():
    assert dias_mes('aug', 2017) == 31

def test_case10():
    assert dias_mes('sep', 2017) == 30

def test_case11():
    assert dias_mes('oct', 2017) == 31

def test_case12():
    assert dias_mes('nov', 2017) == 30

def test_case13():
    assert dias_mes('dec', 2017) == 31

def test_case14():
    assert dias_mes('feb', 2000) == 29

def test_case15():
    assert dias_mes('feb', 1900) == 28

def test_case16():
    assert dias_mes('feb', 2024) == 29

def test_case17():
    with pytest.raises(ValueError):
        dias_mes('MAR', 2017)

def test_case18():
    with pytest.raises(ValueError):
        dias_mes('JAN', 2017)

def test_case19():
    with pytest.raises(ValueError):
        dias_mes('xyz', 2017)

def test_case20():
    with pytest.raises(ValueError):
        dias_mes('February', 2017)
