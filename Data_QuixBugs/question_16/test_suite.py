def test_case001():
    assert lcs_length('witch', 'sandwich') == 2

def test_case002():
    assert lcs_length('meow', 'homeowner') == 4

def test_case003():
    assert lcs_length('fun', '') == 0

def test_case004():
    assert lcs_length('fun', 'function') == 3

def test_case005():
    assert lcs_length('cyborg', 'cyber') == 3

def test_case006():
    assert lcs_length('physics', 'physics') == 7

def test_case007():
    assert lcs_length('space age', 'pace a') == 6

def test_case008():
    assert lcs_length('flippy', 'floppy') == 3

def test_case009():
    assert lcs_length('acbdegcedbg', 'begcfeubk') == 3

