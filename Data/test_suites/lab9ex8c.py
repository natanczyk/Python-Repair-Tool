def test_case1():
    e1 = {(0,0):2, (0,3):1, (1,0):-1, (1,2):1, (2,1):3}
    e2 = {(0,0):4, (1,1):1}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == 8
    assert result[(1,0)] == -4
    assert result[(2,1)] == 3

def test_case2():
    e1 = {(0,0):1, (0,1):2, (1,0):3, (1,1):4}
    e2 = {(0,0):5, (0,1):6, (1,0):7, (1,1):8}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == 19
    assert result[(0,1)] == 22
    assert result[(1,0)] == 43
    assert result[(1,1)] == 50

def test_case3():
    assert prod_esparsa({}, {}) == {}

def test_case4():
    e1 = {(0,0):5}
    assert prod_esparsa(e1, {}) == {}

def test_case5():
    e2 = {(0,0):5}
    assert prod_esparsa({}, e2) == {}

def test_case6():
    e1 = {(0,0):3, (1,1):2}
    e2 = {(0,0):4, (1,1):5}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == 12
    assert result[(1,1)] == 10

def test_case7():
    e1 = {(0,0):2}
    e2 = {(0,0):3}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == 6

def test_case8():
    e1 = {(0,1):2}
    e2 = {(1,0):3}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == 6

def test_case9():
    e1 = {(0,0):2, (0,3):1, (1,0):-1, (1,2):1, (2,1):3}
    e2 = {(0,0):4, (1,1):1}
    result = prod_esparsa(e1, e2)
    assert len(result) == 3

def test_case10():
    e1 = {(0,0):-2, (1,0):3}
    e2 = {(0,0):4, (0,1):1}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == -8
    assert result[(0,1)] == -2
    assert result[(1,0)] == 12
    assert result[(1,1)] == 3

def test_case11():
    e1 = {(0,0):1, (1,1):1}
    e2 = {(0,0):5, (1,1):7}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == 5
    assert result[(1,1)] == 7

def test_case12():
    e1 = {(2,3):4}
    e2 = {(3,2):5}
    result = prod_esparsa(e1, e2)
    assert result[(2,2)] == 20

def test_case13():
    e1 = {(0,0):2, (0,1):3}
    e2 = {(0,0):4}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == 8

def test_case14():
    e1 = {(0,0):1, (0,1):2, (0,2):3}
    e2 = {(0,0):4, (1,0):5, (2,0):6}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == 32

def test_case15():
    e1 = {(0,0):5}
    e2 = {(1,0):3}
    result = prod_esparsa(e1, e2)
    assert result == {}

def test_case16():
    e1 = {(0,0):1, (0,1):2, (1,0):3, (1,1):4}
    e2 = {(0,0):5, (0,1):6, (1,0):7, (1,1):8}
    result = prod_esparsa(e1, e2)
    assert len(result) == 4

def test_case17():
    e1 = {(0,0):1}
    e2 = {(0,0):1}
    assert prod_esparsa(e1, e2) == {(0,0): 1}

def test_case18():
    e1 = {(1,1):5}
    e2 = {(1,1):3}
    result = prod_esparsa(e1, e2)
    assert result[(1,1)] == 15

def test_case19():
    e1 = {(0,0):2, (0,1):2}
    e2 = {(0,0):3, (1,0):3}
    result = prod_esparsa(e1, e2)
    assert result[(0,0)] == 12

def test_case20():
    e1 = {(0,0):2, (0,3):1, (1,0):-1, (1,2):1, (2,1):3}
    e2 = {(0,0):4, (1,1):1}
    result = prod_esparsa(e1, e2)
    assert (0,0) in result
    assert (1,0) in result
    assert (2,1) in result
