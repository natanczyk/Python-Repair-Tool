def test_case1():
    result = euromilhoes()
    assert isinstance(result, list)

def test_case2():
    result = euromilhoes()
    assert len(result) == 2

def test_case3():
    result = euromilhoes()
    assert len(result[0]) == 5

def test_case4():
    result = euromilhoes()
    assert len(result[1]) == 2

def test_case5():
    result = euromilhoes()
    assert all(1 <= x <= 50 for x in result[0])

def test_case6():
    result = euromilhoes()
    assert all(1 <= x <= 12 for x in result[1])

def test_case7():
    result = euromilhoes()
    assert len(set(result[0])) == 5

def test_case8():
    result = euromilhoes()
    assert len(set(result[1])) == 2

def test_case9():
    result = euromilhoes()
    assert result[0] == sorted(result[0])

def test_case10():
    result = euromilhoes()
    assert result[1] == sorted(result[1])

def test_case11():
    for _ in range(5):
        result = euromilhoes()
        assert len(result[0]) == 5

def test_case12():
    for _ in range(5):
        result = euromilhoes()
        assert len(result[1]) == 2

def test_case13():
    for _ in range(5):
        result = euromilhoes()
        assert len(set(result[0])) == 5

def test_case14():
    for _ in range(5):
        result = euromilhoes()
        assert all(1 <= x <= 50 for x in result[0])

def test_case15():
    for _ in range(5):
        result = euromilhoes()
        assert all(1 <= x <= 12 for x in result[1])

def test_case16():
    for _ in range(5):
        result = euromilhoes()
        assert result[0] == sorted(result[0])

def test_case17():
    for _ in range(5):
        result = euromilhoes()
        assert result[1] == sorted(result[1])

def test_case18():
    for _ in range(5):
        result = euromilhoes()
        assert isinstance(result[0], list)
        assert isinstance(result[1], list)

def test_case19():
    for _ in range(10):
        result = euromilhoes()
        assert max(result[0]) <= 50
        assert min(result[0]) >= 1

def test_case20():
    for _ in range(10):
        result = euromilhoes()
        assert max(result[1]) <= 12
        assert min(result[1]) >= 1
