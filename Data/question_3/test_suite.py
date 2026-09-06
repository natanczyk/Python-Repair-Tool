def test_case001():
    assert remove_extras([1, 1, 1, 2, 3]) == [1, 2, 3]

def test_case002():
    assert remove_extras([1, 5, 1, 1, 3, 2]) == [1, 5, 3, 2]

def test_case003():
    assert remove_extras([]) == []

def test_case004():
    assert remove_extras([3, 4, 5, 1, 3]) == [3, 4, 5, 1]

def test_case005():
    assert remove_extras([3, 4, 5, 1, 3]) == [3, 4, 5, 1]

def test_case006():
    assert remove_extras([3, 4, 5, 1, 3]) == [3, 4, 5, 1]

def test_case007():
    # single element — must return it unchanged
    assert remove_extras([1]) == [1]

def test_case008():
    # all same — only first occurrence kept
    assert remove_extras([1, 1, 1, 1]) == [1]

def test_case009():
    # no duplicates — list unchanged; catches inverted condition bug (wrong_3_001)
    assert remove_extras([1, 2, 3]) == [1, 2, 3]

def test_case010():
    # example from problem description
    assert remove_extras([5, 2, 1, 2, 3]) == [5, 2, 1, 3]

def test_case011():
    # alternating duplicates — only first of each kept
    assert remove_extras([1, 2, 1, 2, 1, 2]) == [1, 2]

def test_case012():
    # runs of duplicates
    assert remove_extras([3, 3, 3, 2, 2, 1]) == [3, 2, 1]

def test_case013():
    # duplicate only at the end
    assert remove_extras([1, 2, 3, 3]) == [1, 2, 3]

def test_case014():
    # duplicate only at the start
    assert remove_extras([1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_case015():
    # mixed forward and backward duplicates
    assert remove_extras([5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
