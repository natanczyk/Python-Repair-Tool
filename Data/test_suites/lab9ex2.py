def test_case1():
    assert agrupa_por_chave([('a', 8), ('b', 9), ('a', 3)]) == {'a': [8, 3], 'b': [9]}

def test_case2():
    assert agrupa_por_chave([]) == {}

def test_case3():
    assert agrupa_por_chave([('x', 1)]) == {'x': [1]}

def test_case4():
    assert agrupa_por_chave([('a', 1), ('a', 2), ('a', 3)]) == {'a': [1, 2, 3]}

def test_case5():
    assert agrupa_por_chave([('a', 1), ('b', 2), ('c', 3)]) == {'a': [1], 'b': [2], 'c': [3]}

def test_case6():
    assert agrupa_por_chave([('a', 1), ('b', 2), ('a', 3), ('b', 4)]) == {'a': [1, 3], 'b': [2, 4]}

def test_case7():
    assert agrupa_por_chave([('x', 10), ('y', 20), ('x', 30), ('z', 40)]) == {'x': [10, 30], 'y': [20], 'z': [40]}

def test_case8():
    assert agrupa_por_chave([('a', 3), ('a', 1), ('a', 2)]) == {'a': [3, 1, 2]}

def test_case9():
    assert agrupa_por_chave([('key', 'val')]) == {'key': ['val']}

def test_case10():
    result = agrupa_por_chave([('a', 8), ('b', 9), ('a', 3)])
    assert 'a' in result and 'b' in result

def test_case11():
    result = agrupa_por_chave([('a', 8), ('b', 9), ('a', 3)])
    assert len(result['a']) == 2

def test_case12():
    assert agrupa_por_chave([('m', 1), ('n', 2), ('m', 3), ('n', 4), ('m', 5)]) == {'m': [1, 3, 5], 'n': [2, 4]}

def test_case13():
    result = agrupa_por_chave([('a', 1), ('b', 2)])
    assert sorted(result.keys()) == ['a', 'b']

def test_case14():
    assert agrupa_por_chave([('a', 'x'), ('a', 'y')]) == {'a': ['x', 'y']}

def test_case15():
    assert agrupa_por_chave([('1', 1), ('1', 2), ('2', 3)]) == {'1': [1, 2], '2': [3]}

def test_case16():
    result = agrupa_por_chave([('a', 8), ('b', 9), ('a', 3)])
    assert result['b'] == [9]

def test_case17():
    assert agrupa_por_chave([('k', 0), ('k', 0), ('k', 0)]) == {'k': [0, 0, 0]}

def test_case18():
    result = agrupa_por_chave([('p', 1), ('q', 2), ('r', 3), ('p', 4), ('q', 5)])
    assert result == {'p': [1, 4], 'q': [2, 5], 'r': [3]}

def test_case19():
    assert agrupa_por_chave([('a', True), ('a', False)]) == {'a': [True, False]}

def test_case20():
    result = agrupa_por_chave([('x', i) for i in range(5)])
    assert result == {'x': [0, 1, 2, 3, 4]}
