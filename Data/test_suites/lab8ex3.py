def test_case1():
    assert soma_cumulativa([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]

def test_case2():
    assert soma_cumulativa([1]) == [1]

def test_case3():
    assert soma_cumulativa([]) == []

def test_case4():
    assert soma_cumulativa([5, 5, 5]) == [5, 10, 15]

def test_case5():
    assert soma_cumulativa([1, -1, 1, -1]) == [1, 0, 1, 0]

def test_case6():
    assert soma_cumulativa([0, 0, 0]) == [0, 0, 0]

def test_case7():
    assert soma_cumulativa([10]) == [10]

def test_case8():
    assert soma_cumulativa([1, 2, 3]) == [1, 3, 6]

def test_case9():
    assert soma_cumulativa([2, 4, 6, 8]) == [2, 6, 12, 20]

def test_case10():
    assert soma_cumulativa([100, 200, 300]) == [100, 300, 600]

def test_case11():
    assert soma_cumulativa([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]

def test_case12():
    assert soma_cumulativa([-1, -2, -3]) == [-1, -3, -6]

def test_case13():
    assert soma_cumulativa([3, 0, 0]) == [3, 3, 3]

def test_case14():
    assert soma_cumulativa([10, 20, 30, 40]) == [10, 30, 60, 100]

def test_case15():
    assert soma_cumulativa([0]) == [0]

def test_case16():
    assert soma_cumulativa([5, -5]) == [5, 0]

def test_case17():
    assert soma_cumulativa([1, 2]) == [1, 3]

def test_case18():
    assert soma_cumulativa([0, 1]) == [0, 1]

def test_case19():
    assert soma_cumulativa([4, 3, 2, 1]) == [4, 7, 9, 10]

def test_case20():
    assert soma_cumulativa([10, 10, 10]) == [10, 20, 30]
