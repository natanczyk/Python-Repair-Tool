def test_case1():
    assert seq_racaman(1) == [0]

def test_case2():
    assert seq_racaman(2) == [0, 1]

def test_case3():
    assert seq_racaman(3) == [0, 1, 3]

def test_case4():
    assert seq_racaman(5) == [0, 1, 3, 6, 2]

def test_case5():
    assert seq_racaman(10) == [0, 1, 3, 6, 2, 7, 13, 20, 12, 21]

def test_case6():
    assert seq_racaman(15) == [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9]

def test_case7():
    assert seq_racaman(1)[0] == 0

def test_case8():
    result = seq_racaman(15)
    assert len(result) == 15

def test_case9():
    result = seq_racaman(10)
    assert len(result) == 10

def test_case10():
    result = seq_racaman(5)
    assert all(x >= 0 for x in result)

def test_case11():
    result = seq_racaman(15)
    assert all(x >= 0 for x in result)

def test_case12():
    result = seq_racaman(10)
    assert len(set(result)) == 10

def test_case13():
    result = seq_racaman(15)
    assert len(set(result)) == 15

def test_case14():
    assert seq_racaman(4) == [0, 1, 3, 6]

def test_case15():
    assert seq_racaman(6) == [0, 1, 3, 6, 2, 7]

def test_case16():
    assert seq_racaman(7) == [0, 1, 3, 6, 2, 7, 13]

def test_case17():
    assert seq_racaman(8) == [0, 1, 3, 6, 2, 7, 13, 20]

def test_case18():
    assert seq_racaman(9) == [0, 1, 3, 6, 2, 7, 13, 20, 12]

def test_case19():
    result = seq_racaman(20)
    assert result[0] == 0
    assert len(result) == 20

def test_case20():
    result = seq_racaman(20)
    assert len(set(result)) == 20
