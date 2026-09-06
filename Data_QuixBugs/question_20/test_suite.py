def test_case001():
    assert max_sublist_sum([4, -5, 2, 1, -1, 3]) == 5

def test_case002():
    assert max_sublist_sum([0, -1, 2, -1, 3, -1, 0]) == 4

def test_case003():
    assert max_sublist_sum([3, 4, 5]) == 12

def test_case004():
    assert max_sublist_sum([4, -2, -8, 5, -2, 7, 7, 2, -6, 5]) == 19

def test_case005():
    assert max_sublist_sum([-4, -4, -5]) == 0

def test_case006():
    assert max_sublist_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

