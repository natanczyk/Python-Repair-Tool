def test_case1():
    assert num_para_seq_cod(1234567890) == (9, 4, 1, 6, 3, 8, 5, 0, 7, 2)

def test_case2():
    assert num_para_seq_cod(0) == (2,)

def test_case3():
    assert num_para_seq_cod(8) == (0,)

def test_case4():
    assert num_para_seq_cod(1) == (9,)

def test_case5():
    assert num_para_seq_cod(9) == (7,)

def test_case6():
    assert num_para_seq_cod(2) == (4,)

def test_case7():
    assert num_para_seq_cod(100) == (9, 2, 2)

def test_case8():
    assert num_para_seq_cod(888) == (0, 0, 0)

def test_case9():
    assert num_para_seq_cod(111) == (9, 9, 9)

def test_case10():
    assert num_para_seq_cod(999) == (7, 7, 7)

def test_case11():
    assert num_para_seq_cod(246) == (4, 6, 8)

def test_case12():
    assert num_para_seq_cod(135) == (9, 1, 3)

def test_case13():
    assert num_para_seq_cod(8642) == (0, 8, 6, 4)

def test_case14():
    assert num_para_seq_cod(9753) == (7, 5, 3, 1)

def test_case15():
    assert num_para_seq_cod(468) == (6, 8, 0)

def test_case16():
    assert num_para_seq_cod(1379) == (9, 1, 5, 7)

def test_case17():
    assert num_para_seq_cod(5) == (3,)

def test_case18():
    assert num_para_seq_cod(3) == (1,)

def test_case19():
    assert num_para_seq_cod(7) == (5,)

def test_case20():
    assert num_para_seq_cod(4) == (6,)
