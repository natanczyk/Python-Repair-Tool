def test_case1():
    assert bissexto(1984) == True

def test_case2():
    assert bissexto(1985) == False

def test_case3():
    assert bissexto(2000) == True

def test_case4():
    assert bissexto(1900) == False

def test_case5():
    assert bissexto(2100) == False

def test_case6():
    assert bissexto(2004) == True

def test_case7():
    assert bissexto(1800) == False

def test_case8():
    assert bissexto(2400) == True

def test_case9():
    assert bissexto(2024) == True

def test_case10():
    assert bissexto(2023) == False

def test_case11():
    assert bissexto(1600) == True

def test_case12():
    assert bissexto(1700) == False

def test_case13():
    assert bissexto(2020) == True

def test_case14():
    assert bissexto(2019) == False

def test_case15():
    assert bissexto(1996) == True

def test_case16():
    assert bissexto(1997) == False

def test_case17():
    assert bissexto(2200) == False

def test_case18():
    assert bissexto(2300) == False

def test_case19():
    assert bissexto(2016) == True

def test_case20():
    assert bissexto(2001) == False
