def test_case001():
    assert sort_age([("F", 19)]) == [('F', 19)]

def test_case002():
    assert sort_age([("M", 35), ("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]) == [('M', 35), ('M', 30), ('M', 23), ('F', 19), ('F', 18), ('M', 17)]

def test_case003():
    assert sort_age([("F", 18), ("M", 23), ("F", 19), ("M", 30), ("M", 17)]) == [('M', 30), ('M', 23), ('F', 19), ('F', 18), ('M', 17)]

def test_case004():
    assert sort_age([("F", 18), ("M", 23), ("F", 19), ("M", 30)]) == [('M', 30), ('M', 23), ('F', 19), ('F', 18)]

def test_case005():
    assert sort_age([("M", 23), ("F", 19), ("M", 30)]) == [('M', 30), ('M', 23), ('F', 19)]

def test_case006():
    assert sort_age([]) == []

def test_case007():
    # already sorted descending — output must match input exactly
    assert sort_age([("M", 30), ("F", 20)]) == [("M", 30), ("F", 20)]

def test_case008():
    # reverse order input — must swap
    assert sort_age([("F", 20), ("M", 30)]) == [("M", 30), ("F", 20)]

def test_case009():
    # ascending input, all same gender
    assert sort_age([("M", 1), ("M", 2), ("M", 3)]) == [("M", 3), ("M", 2), ("M", 1)]

def test_case010():
    # extreme age gap
    assert sort_age([("F", 100), ("M", 1)]) == [("F", 100), ("M", 1)]

def test_case011():
    # three elements, mixed genders already partially sorted
    assert sort_age([("F", 50), ("M", 30), ("F", 40)]) == [("F", 50), ("F", 40), ("M", 30)]

def test_case012():
    # five elements in random order; catches lst.pop[i] runtime error (wrong_4_001)
    assert sort_age([("M", 5), ("F", 3), ("M", 1), ("F", 4), ("M", 2)]) == [("M", 5), ("F", 4), ("F", 3), ("M", 2), ("M", 1)]

def test_case013():
    # four elements in ascending order
    assert sort_age([("F", 10), ("M", 20), ("F", 30), ("M", 40)]) == [("M", 40), ("F", 30), ("M", 20), ("F", 10)]

def test_case014():
    # four elements mixed
    assert sort_age([("M", 25), ("F", 15), ("M", 20), ("F", 5)]) == [("M", 25), ("M", 20), ("F", 15), ("F", 5)]

def test_case015():
    # five elements; catches NameError bugs (wrong_4_002/003 reference undefined variables)
    assert sort_age([("F", 33), ("M", 22), ("F", 11), ("M", 44), ("F", 55)]) == [("F", 55), ("M", 44), ("F", 33), ("M", 22), ("F", 11)]
