def test_case1():
    assert filtra_pares([1, 2, 3, 4, 5]) == [2, 4]

def test_case2():
    assert filtra_pares([]) == []

def test_case3():
    assert filtra_pares([1, 3, 5]) == []

def test_case4():
    assert filtra_pares([2, 4, 6]) == [2, 4, 6]

def test_case5():
    assert filtra_pares([1, 2]) == [2]

def test_case6():
    assert filtra_pares([0, 1, 2, 3]) == [0, 2]

def test_case7():
    assert filtra_pares([10, 11, 12]) == [10, 12]

def test_case8():
    result = filtra_pares([1, 2, 3])
    assert isinstance(result, list)

def test_case9():
    assert filtra_pares([2]) == [2]

def test_case10():
    assert filtra_pares([1]) == []

def test_case11():
    assert filtra_pares([100, 101, 200, 201]) == [100, 200]

def test_case12():
    assert filtra_pares([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

def test_case13():
    assert filtra_pares([-4, -3, -2, -1, 0]) == [-4, -2, 0]

def test_case14():
    assert filtra_pares([7, 8, 9, 10]) == [8, 10]

def test_case15():
    assert len(filtra_pares([1, 2, 3, 4, 5])) == 2

def test_case16():
    assert filtra_pares([4, 4, 4]) == [4, 4, 4]

def test_case17():
    assert filtra_pares([1, 3, 5, 7]) == []

def test_case18():
    assert filtra_pares([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]

def test_case19():
    assert filtra_pares([3, 6, 9, 12]) == [6, 12]

def test_case20():
    assert filtra_pares([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]
