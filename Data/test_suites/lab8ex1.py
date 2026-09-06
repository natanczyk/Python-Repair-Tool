def test_case1():
    assert lista_codigos('bom dia') == [98, 111, 109, 32, 100, 105, 97]

def test_case2():
    assert lista_codigos('') == []

def test_case3():
    assert lista_codigos('a') == [97]

def test_case4():
    assert lista_codigos('A') == [65]

def test_case5():
    assert lista_codigos('ABC') == [65, 66, 67]

def test_case6():
    assert lista_codigos('abc') == [97, 98, 99]

def test_case7():
    assert lista_codigos('123') == [49, 50, 51]

def test_case8():
    assert lista_codigos(' ') == [32]

def test_case9():
    assert lista_codigos('!') == [33]

def test_case10():
    assert lista_codigos('\n') == [10]

def test_case11():
    assert lista_codigos('Hello') == [72, 101, 108, 108, 111]

def test_case12():
    assert lista_codigos('z') == [122]

def test_case13():
    assert lista_codigos('0') == [48]

def test_case14():
    assert lista_codigos('Az') == [65, 122]

def test_case15():
    assert lista_codigos('aa') == [97, 97]

def test_case16():
    assert lista_codigos('ba') == [98, 97]

def test_case17():
    assert lista_codigos('ab') == [97, 98]

def test_case18():
    assert lista_codigos('\t') == [9]

def test_case19():
    assert lista_codigos('ZA') == [90, 65]

def test_case20():
    assert lista_codigos('hello') == [104, 101, 108, 108, 111]
