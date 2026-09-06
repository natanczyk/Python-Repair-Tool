def test_case001():
    assert top_k([9, 9, 4, 9, 7, 9, 3, 1, 6], 5) == [9, 9, 9, 9, 7]

def test_case002():
    assert top_k([9, 8, 4, 5, 7, 2, 3, 1, 6], 5) == [9, 8, 7, 6, 5]

def test_case003():
    assert top_k([4, 5, 2, 3, 1, 6], 6) == [6, 5, 4, 3, 2, 1]

def test_case004():
    assert top_k([4, 5, 2, 3, 1, 6], 3) == [6, 5, 4]

def test_case005():
    assert top_k([4, 5, 2, 3, 1, 6], 0) == []

def test_case006():
    # k=1 — catches k>=0 off-by-one bug (wrong_5_001 returns 2 elements)
    assert top_k([1, 2, 3], 1) == [3]

def test_case007():
    # unsorted input, k=2
    assert top_k([3, 1, 2], 2) == [3, 2]

def test_case008():
    # single element list
    assert top_k([1], 1) == [1]

def test_case009():
    # duplicate values, k=2; catches k>=0 bug (returns 3 instead of 2)
    assert top_k([5, 5, 5, 5], 2) == [5, 5]

def test_case010():
    # k equals length of list
    assert top_k([1, 2, 3], 3) == [3, 2, 1]

def test_case011():
    # mixed values
    assert top_k([10, 1, 5, 2, 8], 3) == [10, 8, 5]

def test_case012():
    # ascending input, k=2; catches hardcoded return tmp[:5] (wrong_5_003 returns 5 elements)
    assert top_k([1, 2, 3, 4, 5], 2) == [5, 4]

def test_case013():
    # descending input
    assert top_k([5, 4, 3, 2, 1], 4) == [5, 4, 3, 2]

def test_case014():
    # k=1 with large values; catches k>=0 bug
    assert top_k([100, 50, 1], 1) == [100]

def test_case015():
    # larger list; catches hardcoded [:5] (returns [9,8,7,6,5] instead of [9,8,7,6])
    assert top_k([9, 8, 7, 6, 5, 4, 3, 2, 1], 4) == [9, 8, 7, 6]
