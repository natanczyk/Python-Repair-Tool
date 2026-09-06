def test_case001():
    assert rpn_eval([3.0, 5.0, '+', 2.0, '/']) == 4.0

def test_case002():
    assert rpn_eval([2.0, 2.0, '+']) == 4.0

def test_case003():
    assert rpn_eval([7.0, 4.0, '+', 3.0, '-']) == 8.0

def test_case004():
    assert rpn_eval([1.0, 2.0, '*', 3.0, 4.0, '*', '+']) == 14.0

def test_case005():
    assert rpn_eval([5.0, 9.0, 2.0, '*', '+']) == 23.0

def test_case006():
    assert rpn_eval([5.0, 1.0, 2.0, '+', 4.0, '*', '+', 3.0, '-']) == 14.0

