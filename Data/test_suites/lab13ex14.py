def test_case1():
    assert delta_pos_neg([]) == 0

def test_case2():
    assert delta_pos_neg([1, -2, -1, 3, 1, 2]) == 2

def test_case3():
    assert delta_pos_neg([1, 2, 3]) == 3

def test_case4():
    assert delta_pos_neg([-1, -2, -3]) == -3

def test_case5():
    assert delta_pos_neg([0, 0, 0]) == 0

def test_case6():
    assert delta_pos_neg([1, 0, -1]) == 0

def test_case7():
    assert delta_pos_neg([1]) == 1

def test_case8():
    assert delta_pos_neg([-1]) == -1

def test_case9():
    assert delta_pos_neg([0]) == 0

def test_case10():
    assert delta_pos_neg([5, 3, -2]) == 1

def test_case11():
    assert delta_pos_neg([1, 2, 3, 4, 5]) == 5

def test_case12():
    result = delta_pos_neg([1, -1])
    assert isinstance(result, int)

def test_case13():
    assert delta_pos_neg([1, -1]) == 0

def test_case14():
    assert delta_pos_neg([0, 1, -1, 0, 2, -2]) == 0

def test_case15():
    assert delta_pos_neg([-1, -1, -1, 1]) == -2

def test_case16():
    assert delta_pos_neg([3, -3, 3]) == 1

def test_case17():
    assert delta_pos_neg([0, 0, 1]) == 1

def test_case18():
    assert delta_pos_neg([0, 0, -1]) == -1

def test_case19():
    assert delta_pos_neg([1, 2, -1, -2, 0]) == 0

def test_case20():
    assert delta_pos_neg([10, 20, -5, -3, 0]) == 0
