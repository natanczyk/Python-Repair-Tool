def test_case001():
    assert search(42, (-5, 1, 3, 5, 7, 10)) == 6

def test_case002():
    assert search(42, [1, 5, 10]) == 3

def test_case003():
    assert search(5, (1, 5, 10)) == 1

def test_case004():
    assert search(7, [1, 5, 10]) == 2

def test_case005():
    assert search(3, (1, 5, 10)) == 1

def test_case006():
    assert search(-5, (1, 5, 10)) == 0

def test_case007():
    assert search(10, (-5, -1, 3, 5, 7, 10)) == 5

def test_case008():
    assert search(-100, (-5, -1, 3, 5, 7, 10)) == 0

def test_case009():
    assert search(0, (-5, -1, 3, 5, 7, 10)) == 2

def test_case010():
    assert search(100, []) == 0

def test_case011():
    assert search(-100, ()) == 0

def test_case012():
    # all elements equal x — none strictly less; catches x<e bug returning len(seq)
    assert search(5, [5, 5, 5]) == 0

def test_case013():
    # x appears inside the sequence; catches x<e skipping equal element then returning wrong index
    assert search(2, [1, 2, 3]) == 1

def test_case014():
    # single element equal to x — result must be 0, not 1
    assert search(1, [1]) == 0

def test_case015():
    # single element strictly less than x — result must be 1
    assert search(2, [1]) == 1
