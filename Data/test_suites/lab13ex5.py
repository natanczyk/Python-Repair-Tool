def test_case1():
    assert soma_els_atomicos(()) == 0

def test_case2():
    assert soma_els_atomicos((1, 2, 3)) == 6

def test_case3():
    assert soma_els_atomicos((5,)) == 5

def test_case4():
    assert soma_els_atomicos(((1, 2), (3, 4))) == 10

def test_case5():
    assert soma_els_atomicos((3, ((((((6, (7,))), ), ), ), ), 2, 1)) == 19

def test_case6():
    assert soma_els_atomicos((1, (2, (3, (4,))))) == 10

def test_case7():
    assert soma_els_atomicos((((((5,),),),),)) == 5

def test_case8():
    assert soma_els_atomicos((0, 0, 0)) == 0

def test_case9():
    assert soma_els_atomicos(((1,), (2,), (3,))) == 6

def test_case10():
    assert soma_els_atomicos((10,)) == 10

def test_case11():
    assert soma_els_atomicos((1, (2, 3), (4, (5, 6)))) == 21

def test_case12():
    result = soma_els_atomicos((1, 2, 3))
    assert isinstance(result, int)

def test_case13():
    assert soma_els_atomicos(((((1, 2), 3), 4), 5)) == 15

def test_case14():
    assert soma_els_atomicos((1,)) == 1

def test_case15():
    assert soma_els_atomicos((0,)) == 0

def test_case16():
    assert soma_els_atomicos(((0, 0), (0, 0))) == 0

def test_case17():
    assert soma_els_atomicos((2, (3, (4,)))) == 9

def test_case18():
    assert soma_els_atomicos(((1, (2,)), (3, (4,)))) == 10

def test_case19():
    assert soma_els_atomicos((7, 8, 9)) == 24

def test_case20():
    assert soma_els_atomicos(((1, 2, 3), (4, 5, 6), (7, 8, 9))) == 45
