def test_case1():
    assert num_occ_lista([1, 2, 3, 4, 3], 3) == 2

def test_case2():
    assert num_occ_lista([1, [[[1]], 2], [[[2]]], 2], 2) == 3

def test_case3():
    assert num_occ_lista([1, 2, 3], 4) == 0

def test_case4():
    assert num_occ_lista([1, [1, [1, [1]]]], 1) == 4

def test_case5():
    assert num_occ_lista([], 5) == 0

def test_case6():
    assert num_occ_lista([5, [5], [[5]]], 5) == 3

def test_case7():
    assert num_occ_lista([1, [2, 3], [4, [5, 3]]], 3) == 2

def test_case8():
    assert num_occ_lista([3, [3, [3]]], 3) == 3

def test_case9():
    assert num_occ_lista([1, 2, 3], 1) == 1

def test_case10():
    assert num_occ_lista([[1, 2], [3, 4]], 1) == 1

def test_case11():
    assert num_occ_lista([[1, 2], [3, 4]], 5) == 0

def test_case12():
    assert num_occ_lista([1], 1) == 1

def test_case13():
    assert num_occ_lista([1, [2, [3, [4, [5]]]]], 5) == 1

def test_case14():
    assert num_occ_lista([0, 0, [0, 0]], 0) == 4

def test_case15():
    assert num_occ_lista([1, 1, 1], 1) == 3

def test_case16():
    assert num_occ_lista([[[]]], 1) == 0

def test_case17():
    assert num_occ_lista([2, [2, 2], [[2, 2]]], 2) == 5

def test_case18():
    assert num_occ_lista([1, 2, [3, [4, 3]], 3], 3) == 3

def test_case19():
    assert num_occ_lista([10, [10, [10, [10, [10]]]]], 10) == 5

def test_case20():
    assert num_occ_lista([1, [2, [3]]], 4) == 0
