def test_case001():
    assert shunting_yard([]) == []

def test_case002():
    assert shunting_yard([30]) == [30]

def test_case003():
    assert shunting_yard([10, '-', 5, '-', 2]) == [10, 5, '-', 2, '-']

def test_case004():
    assert shunting_yard([34, '-', 12, '/', 5]) == [34, 12, 5, '/', '-']

def test_case005():
    assert shunting_yard([4, '+', 9, '*', 9, '-', 10, '+', 13]) == [4, 9, 9, '*', '+', 10, '-', 13, '+']

def test_case006():
    assert shunting_yard([7, '*', 43, '-', 7, '+', 13, '/', 7]) == [7, 43, '*', 7, '-', 13, 7, '/', '+']

