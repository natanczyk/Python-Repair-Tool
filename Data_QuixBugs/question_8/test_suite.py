def test_case001():
    assert list(flatten([[1, [], [2, 3]], [[4]], 5])) == [1, 2, 3, 4, 5]

def test_case002():
    assert list(flatten([[], [], [], [], []])) == []

def test_case003():
    assert list(flatten([[], [], 1, [], 1, [], []])) == [1, 1]

def test_case004():
    assert list(flatten([1, 2, 3, [[4]]])) == [1, 2, 3, 4]

def test_case005():
    assert list(flatten([1, 4, 6])) == [1, 4, 6]

def test_case006():
    assert list(flatten(['moe', 'curly', 'larry'])) == ['moe', 'curly', 'larry']

def test_case007():
    assert list(flatten(['a', 'b', ['c'], ['d'], [['e']]])) == ['a', 'b', 'c', 'd', 'e']

