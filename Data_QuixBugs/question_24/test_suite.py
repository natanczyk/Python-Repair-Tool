def test_case001():
    assert next_permutation([3, 2, 4, 1]) == [3, 4, 1, 2]

def test_case002():
    assert next_permutation([3, 5, 6, 2, 1]) == [3, 6, 1, 2, 5]

def test_case003():
    assert next_permutation([3, 5, 6, 2]) == [3, 6, 2, 5]

def test_case004():
    assert next_permutation([4, 5, 1, 7, 9]) == [4, 5, 1, 9, 7]

def test_case005():
    assert next_permutation([4, 5, 8, 7, 1]) == [4, 7, 1, 5, 8]

def test_case006():
    assert next_permutation([9, 5, 2, 6, 1]) == [9, 5, 6, 1, 2]

def test_case007():
    assert next_permutation([44, 5, 1, 7, 9]) == [44, 5, 1, 9, 7]

def test_case008():
    assert next_permutation([3, 4, 5]) == [3, 5, 4]

