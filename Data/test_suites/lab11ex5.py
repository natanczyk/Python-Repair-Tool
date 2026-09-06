def test_case1():
    assert soma_quadrados_impares([1, 2, 3, 4, 5, 6]) == 35

def test_case2():
    assert soma_quadrados_impares([1]) == 1

def test_case3():
    assert soma_quadrados_impares([3, 5, 7]) == 83

def test_case4():
    assert soma_quadrados_impares([2, 3, 4]) == 9

def test_case5():
    assert soma_quadrados_impares([1, 3, 5, 7]) == 84

def test_case6():
    assert soma_quadrados_impares([10, 7, 6, 3]) == 58

def test_case7():
    assert soma_quadrados_impares([11, 22, 33]) == 1210

def test_case8():
    assert soma_quadrados_impares([1, 2]) == 1

def test_case9():
    assert soma_quadrados_impares([9]) == 81

def test_case10():
    assert soma_quadrados_impares([5, 4, 3, 2, 1]) == 35

def test_case11():
    assert soma_quadrados_impares([100, 3, 200, 5]) == 34

def test_case12():
    assert soma_quadrados_impares([7, 7]) == 98

def test_case13():
    result = soma_quadrados_impares([1, 2, 3])
    assert isinstance(result, int)

def test_case14():
    assert soma_quadrados_impares([2, 4, 1]) == 1

def test_case15():
    assert soma_quadrados_impares([1, 3]) == 10

def test_case16():
    assert soma_quadrados_impares([15, 10, 5]) == 250

def test_case17():
    assert soma_quadrados_impares([99, 100]) == 9801

def test_case18():
    assert soma_quadrados_impares([1, 2, 3, 4]) == 10

def test_case19():
    assert soma_quadrados_impares([5, 10, 15]) == 250

def test_case20():
    assert soma_quadrados_impares([2, 5, 8, 11]) == 146
