def test_case001():
    assert possible_change([1, 4, 2], -7) == 0

def test_case002():
    assert possible_change([1, 5, 10, 25], 11) == 4

def test_case003():
    assert possible_change([1, 5, 10, 25], 75) == 121

def test_case004():
    assert possible_change([1, 5, 10, 25], 34) == 18

def test_case005():
    assert possible_change([1, 5, 10], 34) == 16

def test_case006():
    assert possible_change([1, 5, 10, 25], 140) == 568

def test_case007():
    assert possible_change([1, 5, 10, 25, 50], 140) == 786

def test_case008():
    assert possible_change([1, 5, 10, 25, 50, 100], 140) == 817

def test_case009():
    assert possible_change([1, 3, 7, 42, 78], 140) == 981

def test_case010():
    assert possible_change([3, 7, 42, 78], 140) == 20

