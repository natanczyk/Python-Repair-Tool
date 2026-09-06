def test_case1():
    assert junta_ordenados((2, 34, 200, 210), (1, 23)) == (1, 2, 23, 34, 200, 210)

def test_case2():
    assert junta_ordenados((), (1, 2, 3)) == (1, 2, 3)

def test_case3():
    assert junta_ordenados((1, 2, 3), ()) == (1, 2, 3)

def test_case4():
    assert junta_ordenados((), ()) == ()

def test_case5():
    assert junta_ordenados((1,), (2,)) == (1, 2)

def test_case6():
    assert junta_ordenados((5,), (3,)) == (3, 5)

def test_case7():
    assert junta_ordenados((1, 3, 5), (2, 4, 6)) == (1, 2, 3, 4, 5, 6)

def test_case8():
    assert junta_ordenados((1, 1, 2), (1, 3)) == (1, 1, 1, 2, 3)

def test_case9():
    assert junta_ordenados((1, 5, 9), (2, 4)) == (1, 2, 4, 5, 9)

def test_case10():
    assert junta_ordenados((10, 20, 30), (5, 15, 25, 35)) == (5, 10, 15, 20, 25, 30, 35)

def test_case11():
    assert junta_ordenados((100,), (50, 200)) == (50, 100, 200)

def test_case12():
    assert junta_ordenados((1, 2, 3), (4, 5, 6)) == (1, 2, 3, 4, 5, 6)

def test_case13():
    assert junta_ordenados((4, 5, 6), (1, 2, 3)) == (1, 2, 3, 4, 5, 6)

def test_case14():
    assert junta_ordenados((1,), (1,)) == (1, 1)

def test_case15():
    assert junta_ordenados((1, 3), (2, 4)) == (1, 2, 3, 4)

def test_case16():
    assert junta_ordenados((0, 10), (5, 15)) == (0, 5, 10, 15)

def test_case17():
    assert junta_ordenados((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)

def test_case18():
    assert junta_ordenados((3, 4, 5), (1, 2)) == (1, 2, 3, 4, 5)

def test_case19():
    assert junta_ordenados((1, 100), (2, 50, 200)) == (1, 2, 50, 100, 200)

def test_case20():
    assert junta_ordenados((1, 2, 2, 3), (2, 4)) == (1, 2, 2, 2, 3, 4)
