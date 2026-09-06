def test_case001():
    assert hanoi(0, 1, 3) == []

def test_case002():
    assert hanoi(1, 1, 3) == [[1, 3]]

def test_case003():
    assert hanoi(2, 1, 3) == [[1, 2], [1, 3], [2, 3]]

def test_case004():
    assert hanoi(3, 1, 3) == [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]

def test_case005():
    assert hanoi(4, 1, 3) == [[1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3]]

def test_case006():
    assert hanoi(2, 1, 2) == [[1, 3], [1, 2], [3, 2]]

def test_case007():
    assert hanoi(2, 1, 1) == [[1, 2], [1, 1], [2, 1]]

def test_case008():
    assert hanoi(2, 3, 1) == [[3, 2], [3, 1], [2, 1]]

