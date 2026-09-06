def test_case1():
    assert transposta([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_case2():
    assert transposta([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_case3():
    assert transposta([[1]]) == [[1]]

def test_case4():
    assert transposta([[1, 2, 3]]) == [[1], [2], [3]]

def test_case5():
    assert transposta([[1], [2], [3]]) == [[1, 2, 3]]

def test_case6():
    assert transposta([[1, 0], [0, 1]]) == [[1, 0], [0, 1]]

def test_case7():
    assert transposta([[0, 0], [0, 0]]) == [[0, 0], [0, 0]]

def test_case8():
    assert transposta([[1, 2, 3, 4], [5, 6, 7, 8]]) == [[1, 5], [2, 6], [3, 7], [4, 8]]

def test_case9():
    assert transposta([[1, 4], [2, 5], [3, 6]]) == [[1, 2, 3], [4, 5, 6]]

def test_case10():
    assert transposta([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

def test_case11():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    t = transposta(m)
    assert transposta(t) == m

def test_case12():
    assert transposta([[-1, -2], [-3, -4]]) == [[-1, -3], [-2, -4]]

def test_case13():
    assert transposta([[10, 20, 30]]) == [[10], [20], [30]]

def test_case14():
    result = transposta([[1, 2, 3], [4, 5, 6]])
    assert len(result) == 3

def test_case15():
    result = transposta([[1, 2, 3], [4, 5, 6]])
    assert all(len(row) == 2 for row in result)

def test_case16():
    assert transposta([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def test_case17():
    assert transposta([[5], [10], [15], [20]]) == [[5, 10, 15, 20]]

def test_case18():
    assert transposta([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]

def test_case19():
    assert transposta([[100, 200, 300]]) == [[100], [200], [300]]

def test_case20():
    assert transposta([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
