def test_case1():
    assert codifica('abcde') == 'acebd'

def test_case2():
    assert codifica('') == ''

def test_case3():
    assert codifica('a') == 'a'

def test_case4():
    assert codifica('ab') == 'ab'

def test_case5():
    assert codifica('abc') == 'acb'

def test_case6():
    assert codifica('hello') == 'hloel'

def test_case7():
    assert codifica('python') == 'ptoyhn'

def test_case8():
    assert codifica('1234') == '1324'

def test_case9():
    assert codifica('abcdef') == 'acebdf'

def test_case10():
    assert codifica('abcdefghij') == 'acegibdfhj'

def test_case11():
    assert codifica('xy') == 'xy'

def test_case12():
    assert codifica('xyz') == 'xzy'

def test_case13():
    assert codifica('aabb') == 'abab'

def test_case14():
    assert codifica('12345') == '13524'

def test_case15():
    assert codifica('aaaaaa') == 'aaaaaa'

def test_case16():
    assert codifica('abba') == 'abba'

def test_case17():
    assert codifica('world') == 'wrdol'

def test_case18():
    assert codifica('test') == 'tset'

def test_case19():
    assert codifica('coding') == 'cdnoig'

def test_case20():
    assert codifica('ababab') == 'aaabbb'
