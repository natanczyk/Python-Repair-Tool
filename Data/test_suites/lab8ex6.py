def test_case1():
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert soma_mat(m1, m2) == [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

def test_case2():
    assert soma_mat([[1, 0], [0, 1]], [[0, 1], [1, 0]]) == [[1, 1], [1, 1]]

def test_case3():
    assert soma_mat([[0, 0], [0, 0]], [[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

def test_case4():
    assert soma_mat([[1, 2], [3, 4]], [[0, 0], [0, 0]]) == [[1, 2], [3, 4]]

def test_case5():
    assert soma_mat([[1]], [[2]]) == [[3]]

def test_case6():
    assert soma_mat([[1, 1], [1, 1]], [[1, 1], [1, 1]]) == [[2, 2], [2, 2]]

def test_case7():
    assert soma_mat([[-1, 2], [3, -4]], [[1, -2], [-3, 4]]) == [[0, 0], [0, 0]]

def test_case8():
    assert soma_mat([[5, 0], [0, 5]], [[5, 0], [0, 5]]) == [[10, 0], [0, 10]]

def test_case9():
    assert soma_mat([[0]], [[0]]) == [[0]]

def test_case10():
    assert soma_mat([[1, 2, 3]], [[4, 5, 6]]) == [[5, 7, 9]]

def test_case11():
    assert soma_mat([[10, 20], [30, 40]], [[1, 2], [3, 4]]) == [[11, 22], [33, 44]]

def test_case12():
    assert soma_mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                   [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == [[2, 0, 0], [0, 2, 0], [0, 0, 2]]

def test_case13():
    assert soma_mat([[-1]], [[1]]) == [[0]]

def test_case14():
    assert soma_mat([[100, 200]], [[300, 400]]) == [[400, 600]]

def test_case15():
    assert soma_mat([[1, 2], [3, 4], [5, 6]], [[6, 5], [4, 3], [2, 1]]) == [[7, 7], [7, 7], [7, 7]]

def test_case16():
    result = soma_mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert len(result) == 3

def test_case17():
    result = soma_mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert all(len(row) == 3 for row in result)

def test_case18():
    assert soma_mat([[2, 4], [6, 8]], [[8, 6], [4, 2]]) == [[10, 10], [10, 10]]

def test_case19():
    assert soma_mat([[1, 1, 1], [2, 2, 2]], [[0, 1, 2], [0, 1, 2]]) == [[1, 2, 3], [2, 3, 4]]

def test_case20():
    assert soma_mat([[-5, -3], [-1, 0]], [[5, 3], [1, 0]]) == [[0, 0], [0, 0]]
