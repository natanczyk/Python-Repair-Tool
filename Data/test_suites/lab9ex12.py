def test_case1():
    pubs = {'A': 10, 'B': 5, 'C': 4, 'D': 3, 'E': 8}
    assert h_index(pubs) == 4

def test_case2():
    assert h_index({}) == 0

def test_case3():
    assert h_index({'A': 1}) == 1

def test_case4():
    assert h_index({'A': 0}) == 0

def test_case5():
    pubs = {'A': 3, 'B': 3, 'C': 3}
    assert h_index(pubs) == 3

def test_case6():
    pubs = {'A': 5, 'B': 5}
    assert h_index(pubs) == 2

def test_case7():
    pubs = {'A': 10, 'B': 10, 'C': 10, 'D': 10, 'E': 10}
    assert h_index(pubs) == 5

def test_case8():
    pubs = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
    assert h_index(pubs) == 3

def test_case9():
    pubs = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
    assert h_index(pubs) == 1

def test_case10():
    pubs = {'A': 7, 'B': 6, 'C': 5, 'D': 4}
    assert h_index(pubs) == 4

def test_case11():
    pubs = {'A': 100}
    assert h_index(pubs) == 1

def test_case12():
    pubs = {'A': 2, 'B': 2}
    assert h_index(pubs) == 2

def test_case13():
    pubs = {'A': 0, 'B': 0, 'C': 0}
    assert h_index(pubs) == 0

def test_case14():
    pubs = {'A': 10, 'B': 8, 'C': 5, 'D': 4, 'E': 3}
    assert h_index(pubs) == 4

def test_case15():
    result = h_index({'A': 5, 'B': 3})
    assert isinstance(result, int)

def test_case16():
    pubs = {'P1': 6, 'P2': 6, 'P3': 6, 'P4': 6, 'P5': 6, 'P6': 6}
    assert h_index(pubs) == 6

def test_case17():
    pubs = {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 1}
    assert h_index(pubs) == 4

def test_case18():
    pubs = {'A': 3, 'B': 3, 'C': 3, 'D': 3, 'E': 3}
    assert h_index(pubs) == 3

def test_case19():
    pubs = {'A': 10, 'B': 1}
    assert h_index(pubs) == 1

def test_case20():
    pubs = {'A': 5, 'B': 5, 'C': 5, 'D': 5, 'E': 5}
    assert h_index(pubs) == 5
