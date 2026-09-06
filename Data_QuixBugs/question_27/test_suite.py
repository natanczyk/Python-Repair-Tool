def test_case001():
    assert powerset(['a', 'b', 'c']) == [[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]

def test_case002():
    assert powerset(['a', 'b']) == [[], ['b'], ['a'], ['a', 'b']]

def test_case003():
    assert powerset(['a']) == [[], ['a']]

def test_case004():
    assert powerset([]) == [[]]

def test_case005():
    assert powerset(['x', 'df', 'z', 'm']) == [[], ['m'], ['z'], ['z', 'm'], ['df'], ['df', 'm'], ['df', 'z'], ['df', 'z', 'm'], ['x'], ['x', 'm'], ['x', 'z'], ['x', 'z', 'm'], ['x', 'df'], ['x', 'df', 'm'], ['x', 'df', 'z'], ['x', 'df', 'z', 'm']]

