def test_case1():
    assert num_dig(1) == 1

def test_case2():
    assert num_dig(9) == 1

def test_case3():
    assert num_dig(10) == 2

def test_case4():
    assert num_dig(99) == 2

def test_case5():
    assert num_dig(100) == 3

def test_case6():
    assert num_dig(999) == 3

def test_case7():
    assert num_dig(1000) == 4

def test_case8():
    assert num_dig(9999) == 4

def test_case9():
    assert num_dig(10000) == 5

def test_case10():
    assert num_dig(12345) == 5

def test_case11():
    assert num_dig(5) == 1

def test_case12():
    assert num_dig(50) == 2

def test_case13():
    assert num_dig(500) == 3

def test_case14():
    assert num_dig(5000) == 4

def test_case15():
    assert num_dig(50000) == 5

def test_case16():
    result = num_dig(123)
    assert isinstance(result, int)

def test_case17():
    assert num_dig(1234567890) == 10

def test_case18():
    assert num_dig(11) == 2

def test_case19():
    assert num_dig(111) == 3

def test_case20():
    assert num_dig(1111) == 4
