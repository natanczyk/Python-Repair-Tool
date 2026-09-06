def test_case1():
    cc = 'a aranha arranha a ra a ra arranha a aranha nem a aranha arranha a ra nem a ra arranha a aranha'
    result = conta_palavras(cc)
    assert result == {'a': 8, 'aranha': 4, 'arranha': 4, 'ra': 4, 'nem': 2}

def test_case2():
    assert conta_palavras('hello world hello') == {'hello': 2, 'world': 1}

def test_case3():
    assert conta_palavras('a') == {'a': 1}

def test_case4():
    assert conta_palavras('') == {}

def test_case5():
    assert conta_palavras('one two three') == {'one': 1, 'two': 1, 'three': 1}

def test_case6():
    assert conta_palavras('the the the') == {'the': 3}

def test_case7():
    result = conta_palavras('a b c a b a')
    assert result == {'a': 3, 'b': 2, 'c': 1}

def test_case8():
    result = conta_palavras('x x x x x')
    assert result == {'x': 5}

def test_case9():
    result = conta_palavras('hello hello world world world')
    assert result['hello'] == 2
    assert result['world'] == 3

def test_case10():
    result = conta_palavras('a aranha arranha a ra a ra arranha a aranha nem a aranha arranha a ra nem a ra arranha a aranha')
    assert result['a'] == 8

def test_case11():
    result = conta_palavras('hello world hello')
    assert isinstance(result, dict)

def test_case12():
    result = conta_palavras('one two three')
    assert len(result) == 3

def test_case13():
    result = conta_palavras('python python python java java c')
    assert result == {'python': 3, 'java': 2, 'c': 1}

def test_case14():
    result = conta_palavras('a b c a b a')
    assert sum(result.values()) == 6

def test_case15():
    result = conta_palavras('word')
    assert result == {'word': 1}

def test_case16():
    result = conta_palavras('a b c a b c a b c')
    assert result == {'a': 3, 'b': 3, 'c': 3}

def test_case17():
    result = conta_palavras('hello world')
    assert 'hello' in result
    assert 'world' in result

def test_case18():
    result = conta_palavras('a a a a')
    assert result['a'] == 4

def test_case19():
    result = conta_palavras('abc abc def ghi ghi ghi')
    assert result == {'abc': 2, 'def': 1, 'ghi': 3}

def test_case20():
    result = conta_palavras('x y z x y x')
    assert result['x'] == 3
    assert result['y'] == 2
    assert result['z'] == 1
