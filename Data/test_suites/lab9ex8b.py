def test_case1():
    e1 = {(1, 5): 4, (2, 3): 9, (4, 1): 1}
    e2 = {(1, 6): 2, (4, 1): 2, (5, 4): 2}
    result = soma_esparsa(e1, e2)
    assert result[(1, 5)] == 4
    assert result[(2, 3)] == 9
    assert result[(4, 1)] == 3
    assert result[(1, 6)] == 2
    assert result[(5, 4)] == 2

def test_case2():
    assert soma_esparsa({}, {}) == {}

def test_case3():
    result = soma_esparsa({}, {(1, 1): 5})
    assert result == {(1, 1): 5}

def test_case4():
    result = soma_esparsa({(1, 1): 5}, {})
    assert result == {(1, 1): 5}

def test_case5():
    e1 = {(1, 1): 2}
    e2 = {(2, 2): 3}
    result = soma_esparsa(e1, e2)
    assert result == {(1, 1): 2, (2, 2): 3}

def test_case6():
    e1 = {(1, 1): 2, (2, 2): 3}
    e2 = {(1, 1): 8, (2, 2): 7}
    result = soma_esparsa(e1, e2)
    assert result[(1, 1)] == 10
    assert result[(2, 2)] == 10

def test_case7():
    e1 = {(0, 0): 1, (1, 1): 2}
    e2 = {(0, 0): 4, (2, 2): 3}
    result = soma_esparsa(e1, e2)
    assert result[(0, 0)] == 5
    assert result[(1, 1)] == 2
    assert result[(2, 2)] == 3

def test_case8():
    e1 = {(1, 5): 4, (2, 3): 9, (4, 1): 1}
    e2 = {(1, 6): 2, (4, 1): 2, (5, 4): 2}
    result = soma_esparsa(e1, e2)
    assert len(result) == 5

def test_case9():
    e1 = {(0, 0): 10}
    e2 = {(0, 0): 5}
    result = soma_esparsa(e1, e2)
    assert result[(0, 0)] == 15

def test_case10():
    e1 = {(1, 2): 100, (3, 4): 200}
    e2 = {(5, 6): 300}
    result = soma_esparsa(e1, e2)
    assert result[(1, 2)] == 100
    assert result[(3, 4)] == 200
    assert result[(5, 6)] == 300

def test_case11():
    e1 = {(0, 0): 5, (0, 1): 3}
    e2 = {(0, 0): 2, (1, 0): 7}
    result = soma_esparsa(e1, e2)
    assert result[(0, 0)] == 7
    assert result[(0, 1)] == 3
    assert result[(1, 0)] == 7

def test_case12():
    e1 = {(2, 3): 9}
    e2 = {(2, 3): 1}
    result = soma_esparsa(e1, e2)
    assert result[(2, 3)] == 10

def test_case13():
    e1 = {(1, 5): 4, (2, 3): 9, (4, 1): 1}
    e2 = {(1, 6): 2, (4, 1): 2, (5, 4): 2}
    result = soma_esparsa(e1, e2)
    assert (2, 3) in result

def test_case14():
    e1 = {(1, 5): 4, (2, 3): 9, (4, 1): 1}
    e2 = {(1, 6): 2, (4, 1): 2, (5, 4): 2}
    result = soma_esparsa(e1, e2)
    assert (1, 5) in result and (1, 6) in result

def test_case15():
    e1 = {(0, 0): -5}
    e2 = {(0, 0): 5}
    result = soma_esparsa(e1, e2)
    assert result[(0, 0)] == 0

def test_case16():
    e1 = {(1, 1): 3, (2, 2): 6}
    e2 = {(1, 1): 3, (3, 3): 9}
    result = soma_esparsa(e1, e2)
    assert result[(1, 1)] == 6
    assert result[(2, 2)] == 6
    assert result[(3, 3)] == 9

def test_case17():
    e1 = {(0, 5): 1, (5, 0): 2}
    e2 = {(0, 5): 4, (5, 0): 3}
    result = soma_esparsa(e1, e2)
    assert result[(0, 5)] == 5
    assert result[(5, 0)] == 5

def test_case18():
    e1 = {(i, i): i for i in range(5)}
    result = soma_esparsa(e1, {})
    for i in range(5):
        assert result[(i, i)] == i

def test_case19():
    e1 = {(1, 1): 1}
    e2 = {(1, 1): 1, (2, 2): 1}
    result = soma_esparsa(e1, e2)
    assert result[(1, 1)] == 2
    assert result[(2, 2)] == 1

def test_case20():
    e1 = {(100, 200): 999}
    e2 = {(100, 200): 1}
    result = soma_esparsa(e1, e2)
    assert result[(100, 200)] == 1000
