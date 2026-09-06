def test_case1():
    assert multiplica_mat([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]

def test_case2():
    assert multiplica_mat([[1, 0], [0, 1]], [[5, 6], [7, 8]]) == [[5, 6], [7, 8]]

def test_case3():
    assert multiplica_mat([[5, 6], [7, 8]], [[1, 0], [0, 1]]) == [[5, 6], [7, 8]]

def test_case4():
    assert multiplica_mat([[1, 2, 3], [4, 5, 6]],
                   [[7, 8], [9, 10], [11, 12]]) == [[58, 64], [139, 154]]

def test_case5():
    assert multiplica_mat([[2]], [[3]]) == [[6]]

def test_case6():
    assert multiplica_mat([[1, 1], [1, 1]], [[1, 1], [1, 1]]) == [[2, 2], [2, 2]]

def test_case7():
    assert multiplica_mat([[0, 0], [0, 0]], [[1, 2], [3, 4]]) == [[0, 0], [0, 0]]

def test_case8():
    assert multiplica_mat([[1, 2, 3]], [[1], [2], [3]]) == [[14]]

def test_case9():
    assert multiplica_mat([[1], [2], [3]], [[1, 2, 3]]) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

def test_case10():
    assert multiplica_mat([[2, 0], [0, 2]], [[3, 1], [1, 3]]) == [[6, 2], [2, 6]]

def test_case11():
    assert multiplica_mat([[1, 2], [3, 4]], [[1, 0], [0, 1]]) == [[1, 2], [3, 4]]

def test_case12():
    assert multiplica_mat([[2, 3], [1, 4]], [[5, 2], [3, 1]]) == [[19, 7], [17, 6]]

def test_case13():
    assert multiplica_mat([[-1, 2], [3, -4]], [[1, 2], [3, 4]]) == [[5, 6], [-9, -10]]

def test_case14():
    assert multiplica_mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                   [[4, 5, 6], [7, 8, 9], [1, 2, 3]]) == [[4, 5, 6], [7, 8, 9], [1, 2, 3]]

def test_case15():
    assert multiplica_mat([[1, 2]], [[3], [4]]) == [[11]]

def test_case16():
    result = multiplica_mat([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    assert len(result) == 2
    assert all(len(row) == 2 for row in result)

def test_case17():
    result = multiplica_mat([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    assert len(result) == 2
    assert all(len(row) == 2 for row in result)

def test_case18():
    assert multiplica_mat([[10]], [[10]]) == [[100]]

def test_case19():
    assert multiplica_mat([[1, 1, 1], [1, 1, 1]], [[1, 1], [1, 1], [1, 1]]) == [[3, 3], [3, 3]]

def test_case20():
    assert multiplica_mat([[0]], [[99]]) == [[0]]
