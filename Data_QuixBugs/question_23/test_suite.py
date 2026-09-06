def test_case001():
    assert next_palindrome([1, 4, 9, 4, 1]) == [1, 5, 0, 5, 1]

def test_case002():
    assert next_palindrome([1, 3, 1]) == [1, 4, 1]

def test_case003():
    assert next_palindrome([4, 7, 2, 5, 5, 2, 7, 4]) == [4, 7, 2, 6, 6, 2, 7, 4]

def test_case004():
    assert next_palindrome([4, 7, 2, 5, 2, 7, 4]) == [4, 7, 2, 6, 2, 7, 4]

def test_case005():
    assert next_palindrome([9, 9, 9]) == [1, 0, 0, 1]

