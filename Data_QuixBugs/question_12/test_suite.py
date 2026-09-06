def test_case001():
    assert is_valid_parenthesization('((()()))()') == True

def test_case002():
    assert is_valid_parenthesization(')()(') == False

def test_case003():
    assert is_valid_parenthesization('((') == False

