def test_case001():
    assert lis([]) == 0

def test_case002():
    assert lis([3]) == 1

def test_case003():
    assert lis([10, 20, 11, 32, 22, 48, 43]) == 4

def test_case004():
    assert lis([4, 2, 1]) == 1

def test_case005():
    assert lis([5, 1, 3, 4, 7]) == 4

def test_case006():
    assert lis([4, 1]) == 1

def test_case007():
    assert lis([-1, 0, 2]) == 3

def test_case008():
    assert lis([0, 2]) == 2

def test_case009():
    assert lis([4, 1, 5, 3, 7, 6, 2]) == 3

def test_case010():
    assert lis([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6

def test_case011():
    assert lis([7, 10, 9, 2, 3, 8, 1]) == 3

def test_case012():
    assert lis([9, 11, 2, 13, 7, 15]) == 4

