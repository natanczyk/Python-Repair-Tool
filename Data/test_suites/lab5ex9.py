def test_case1():
    assert dia_da_semana(18, 1, 2014) == 'sabado'

def test_case2():
    assert dia_da_semana(1, 1, 2000) == 'sabado'

def test_case3():
    assert dia_da_semana(25, 12, 2023) == 'segunda'

def test_case4():
    assert dia_da_semana(4, 7, 2024) == 'quinta'

def test_case5():
    assert dia_da_semana(29, 2, 2000) == 'terca'

def test_case6():
    assert dia_da_semana(15, 3, 2023) == 'quarta'

def test_case7():
    assert dia_da_semana(11, 11, 1918) == 'segunda'

def test_case8():
    assert dia_da_semana(9, 9, 2001) == 'domingo'

def test_case9():
    assert dia_da_semana(31, 10, 2023) == 'terca'

def test_case10():
    assert dia_da_semana(5, 5, 2005) == 'quinta'

def test_case11():
    assert dia_da_semana(24, 8, 2011) == 'quarta'

def test_case12():
    assert dia_da_semana(14, 2, 2020) == 'sexta'

def test_case13():
    assert dia_da_semana(1, 1, 2026) == 'quinta'

def test_case14():
    assert dia_da_semana(1, 4, 2025) == 'terca'

def test_case15():
    assert dia_da_semana(15, 6, 2020) == 'segunda'

def test_case16():
    assert dia_da_semana(1, 1, 1900) == 'segunda'

def test_case17():
    assert dia_da_semana(6, 8, 1945) == 'segunda'

def test_case18():
    assert dia_da_semana(20, 7, 1969) == 'domingo'

def test_case19():
    assert dia_da_semana(26, 12, 2004) == 'domingo'

def test_case20():
    assert dia_da_semana(22, 11, 1963) == 'sexta'
