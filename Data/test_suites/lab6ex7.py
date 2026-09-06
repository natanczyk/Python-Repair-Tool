def test_case1():
    assert amigas('amigas', 'amigas') == True

def test_case2():
    assert amigas('amigas', 'asigos') == False

def test_case3():
    assert amigas('abc', 'abc') == True

def test_case4():
    assert amigas('abc', 'abd') == False

def test_case5():
    assert amigas('abcdefghijk', 'abcdefghijl') == True

def test_case6():
    assert amigas('abcdefghijk', 'xbcdefghijk') == True

def test_case7():
    assert amigas('abcdefghijk', 'xbcyefghijk') == False

def test_case8():
    assert amigas('hello', 'hello') == True

def test_case9():
    assert amigas('hello', 'world') == False

def test_case10():
    assert amigas('a', 'a') == True

def test_case11():
    assert amigas('a', 'b') == False

def test_case12():
    assert amigas('ab', 'cd') == False

def test_case13():
    assert amigas('abc', 'abcdef') == False

def test_case14():
    assert amigas('abcdefghij', 'xbcdefghij') == False

def test_case15():
    assert amigas('abcdefghijk', 'abcdefghijk') == True

def test_case16():
    assert amigas('amigas', 'amigos') == False

def test_case17():
    assert amigas('python', 'python') == True

def test_case18():
    assert amigas('aaaaaaaaaaa', 'aaaaaaaaaab') == True

def test_case19():
    assert amigas('aaaaaaaaaa', 'aaaaaaaaab') == False

def test_case20():
    assert amigas('abcde', 'fghij') == False
