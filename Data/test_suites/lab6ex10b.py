def test_case1():
    assert descodifica('acebd') == 'abcde'

def test_case2():
    assert descodifica('') == ''

def test_case3():
    assert descodifica('a') == 'a'

def test_case4():
    assert descodifica('ab') == 'ab'

def test_case5():
    assert descodifica('acb') == 'abc'

def test_case6():
    assert descodifica('hloel') == 'hello'

def test_case7():
    assert descodifica('ptoyhn') == 'python'

def test_case8():
    assert descodifica('1324') == '1234'

def test_case9():
    assert descodifica('acebdf') == 'abcdef'

def test_case10():
    assert descodifica('acegibdfhj') == 'abcdefghij'

def test_case11():
    assert descodifica('xy') == 'xy'

def test_case12():
    assert descodifica('xzy') == 'xyz'

def test_case13():
    assert descodifica('abab') == 'aabb'

def test_case14():
    assert descodifica('13524') == '12345'

def test_case15():
    assert descodifica('aaaaaa') == 'aaaaaa'

def test_case16():
    assert descodifica('abba') == 'abba'

def test_case17():
    assert descodifica('wrdol') == 'world'

def test_case18():
    assert descodifica('tset') == 'test'

def test_case19():
    assert descodifica('cdnoig') == 'coding'

def test_case20():
    assert descodifica('aaabbb') == 'ababab'
