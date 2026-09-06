def test_case001():
    assert levenshtein('electron', 'neutron') == 3

def test_case002():
    assert levenshtein('kitten', 'sitting') == 3

def test_case003():
    assert levenshtein('rosettacode', 'raisethysword') == 8

def test_case004():
    assert levenshtein('amanaplanacanalpanama', 'docnoteidissentafastneverpreventsafatnessidietoncod') == 42

def test_case005():
    assert levenshtein('abcdefg', 'gabcdef') == 2

def test_case006():
    assert levenshtein('', '') == 0

def test_case007():
    assert levenshtein('hello', 'olleh') == 4

