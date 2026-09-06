def test_case1():
    assert soma_fn(4, lambda x: x * x) == 30

def test_case2():
    assert soma_fn(4, lambda x: x + 1) == 14

def test_case3():
    assert soma_fn(1, lambda x: x * x) == 1

def test_case4():
    assert soma_fn(5, lambda x: x) == 15

def test_case5():
    assert soma_fn(3, lambda x: x * x) == 14

def test_case6():
    assert soma_fn(10, lambda x: x) == 55

def test_case7():
    assert soma_fn(1, lambda x: x + 1) == 2

def test_case8():
    assert soma_fn(5, lambda x: x * x) == 55

def test_case9():
    assert soma_fn(2, lambda x: x ** 3) == 9

def test_case10():
    assert soma_fn(6, lambda x: x) == 21

def test_case11():
    assert soma_fn(100, lambda x: x) == 5050

def test_case12():
    assert soma_fn(3, lambda x: 2 * x) == 12

def test_case13():
    assert soma_fn(1, lambda x: x) == 1

def test_case14():
    assert soma_fn(4, lambda x: x) == 10

def test_case15():
    assert soma_fn(2, lambda x: x * x) == 5

def test_case16():
    assert soma_fn(5, lambda x: x + 2) == 25

def test_case17():
    assert soma_fn(3, lambda x: x + 1) == 9

def test_case18():
    result = soma_fn(4, lambda x: x * x)
    assert isinstance(result, int)

def test_case19():
    assert soma_fn(6, lambda x: x * x) == 91

def test_case20():
    assert soma_fn(2, lambda x: x + 1) == 5
