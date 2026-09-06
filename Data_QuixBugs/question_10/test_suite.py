def test_case001():
    assert get_factors(1) == []

def test_case002():
    assert get_factors(100) == [2, 2, 5, 5]

def test_case003():
    assert get_factors(101) == [101]

def test_case004():
    assert get_factors(104) == [2, 2, 2, 13]

def test_case005():
    assert get_factors(2) == [2]

def test_case006():
    assert get_factors(3) == [3]

def test_case007():
    assert get_factors(17) == [17]

def test_case008():
    assert get_factors(63) == [3, 3, 7]

def test_case009():
    assert get_factors(74) == [2, 37]

def test_case010():
    assert get_factors(73) == [73]

def test_case011():
    assert get_factors(9837) == [3, 3, 1093]

