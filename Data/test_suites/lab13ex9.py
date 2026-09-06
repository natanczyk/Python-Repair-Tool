def test_case1():
    assert parte([], 5) == ([], [])

def test_case2():
    assert parte([1, 2, 3, 4, 5], 3) == ([1, 2], [3, 4, 5])

def test_case3():
    assert parte([3, 1, 4, 1, 5, 9, 2, 6], 4) == ([3, 1, 1, 2], [4, 5, 9, 6])

def test_case4():
    assert parte([1, 1, 1], 1) == ([], [1, 1, 1])

def test_case5():
    assert parte([1, 1, 1], 2) == ([1, 1, 1], [])

def test_case6():
    assert parte([5, 3, 8, 1, 9], 5) == ([3, 1], [5, 8, 9])

def test_case7():
    assert parte([1], 1) == ([], [1])

def test_case8():
    assert parte([1], 2) == ([1], [])

def test_case9():
    assert parte([3, 3, 3], 3) == ([], [3, 3, 3])

def test_case10():
    assert parte([1, 2, 3, 4, 5], 6) == ([1, 2, 3, 4, 5], [])

def test_case11():
    assert parte([1, 2, 3, 4, 5], 1) == ([], [1, 2, 3, 4, 5])

def test_case12():
    result = parte([1, 2, 3], 2)
    assert isinstance(result, tuple)

def test_case13():
    assert parte([5, 2, 8, 1, 9, 3], 5) == ([2, 1, 3], [5, 8, 9])

def test_case14():
    assert parte([10, 20, 30], 20) == ([10], [20, 30])

def test_case15():
    assert parte([0, 1, 2, 3], 2) == ([0, 1], [2, 3])

def test_case16():
    assert parte([-3, -1, 0, 2], 0) == ([-3, -1], [0, 2])

def test_case17():
    assert parte([4, 4, 4, 4], 4) == ([], [4, 4, 4, 4])

def test_case18():
    first, second = parte([1, 2, 3, 4, 5], 3)
    assert len(first) + len(second) == 5

def test_case19():
    assert parte([7, 2, 5, 1, 8], 5) == ([2, 1], [7, 5, 8])

def test_case20():
    assert parte([1, 3, 5, 7], 4) == ([1, 3], [5, 7])
