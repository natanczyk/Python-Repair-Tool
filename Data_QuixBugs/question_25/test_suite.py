def test_case001():
    assert pascal(1) == [[1]]

def test_case002():
    assert pascal(2) == [[1], [1, 1]]

def test_case003():
    assert pascal(3) == [[1], [1, 1], [1, 2, 1]]

def test_case004():
    assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

def test_case005():
    assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

