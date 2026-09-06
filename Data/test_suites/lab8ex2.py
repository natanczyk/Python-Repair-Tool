def test_case1():
    assert remove_multiplos([2, 3, 5, 9, 12, 33, 34, 45], 3) == [2, 5, 34]

def test_case2():
    assert remove_multiplos([1, 2, 3, 4, 5, 6], 2) == [1, 3, 5]

def test_case3():
    assert remove_multiplos([], 3) == []

def test_case4():
    assert remove_multiplos([1, 2, 3], 5) == [1, 2, 3]

def test_case5():
    assert remove_multiplos([3, 6, 9], 3) == []

def test_case6():
    assert remove_multiplos([0, 1, 2, 3], 2) == [1, 3]

def test_case7():
    assert remove_multiplos([4, 8, 12], 4) == []

def test_case8():
    assert remove_multiplos([1, 4, 9, 16], 4) == [1, 9]

def test_case9():
    assert remove_multiplos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == [1, 2, 3, 4, 6, 7, 8, 9]

def test_case10():
    assert remove_multiplos([2, 4, 6, 8, 10], 2) == []

def test_case11():
    assert remove_multiplos([1, 3, 7, 11], 2) == [1, 3, 7, 11]

def test_case12():
    assert remove_multiplos([1, 2, 4, 8], 4) == [1, 2]

def test_case13():
    assert remove_multiplos([6, 12, 18, 24, 5], 6) == [5]

def test_case14():
    assert remove_multiplos([7, 14, 21], 7) == []

def test_case15():
    assert remove_multiplos([0, 3, 6, 9], 3) == []

def test_case16():
    assert remove_multiplos([1], 1) == []

def test_case17():
    assert remove_multiplos([1], 2) == [1]

def test_case18():
    assert remove_multiplos([100, 101, 102, 103], 10) == [101, 103]

def test_case19():
    assert remove_multiplos([5, 10, 15, 20, 25], 5) == []

def test_case20():
    assert remove_multiplos([2, 3, 5, 7, 11, 13], 2) == [3, 5, 7, 11, 13]
