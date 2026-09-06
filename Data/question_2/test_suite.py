def test_case001():
    assert unique_day("1", (("January","1"),("February","1"))) == False

def test_case002():
    assert unique_month("January", (("January","1"),("January","2"))) == False

def test_case003():
    assert unique_month("January", (("January","1"),("February","1"))) == True

def test_case004():
    assert contains_unique_day("January", (("January","1"),("January","2"))) == True

def test_case005():
    assert contains_unique_day("January", (("January","1"),("February","1"))) == False

def test_case006():
    assert contains_unique_day("February", (("January","10"),("February","1"),("February","10"))) == True

def test_case007():
    assert unique_day("3", (("January","1"),("January","2"))) == False

def test_case008():
    assert unique_month("March", (("January","1"),("February","1"))) == False

def test_case009():
    assert unique_day("1", (("January","1"),("January","2"))) == True

def test_case010():
    assert unique_day("16", tuple_of_possible_birthdays) == False

def test_case011():
    assert unique_day("17", tuple_of_possible_birthdays) == False

def test_case012():
    assert unique_day("18", tuple_of_possible_birthdays) == True

def test_case013():
    assert unique_day("19", tuple_of_possible_birthdays) == True

def test_case014():
    assert unique_month("May", tuple_of_possible_birthdays) == False

def test_case015():
    assert unique_month("June", tuple_of_possible_birthdays) == False

def test_case016():
    assert contains_unique_day("June", tuple_of_possible_birthdays) == True

def test_case017():
    assert contains_unique_day("July", tuple_of_possible_birthdays) == False

def test_case018():
    # month has TWO unique days — catches len(days)==1 bug (should be >=1)
    assert contains_unique_day("May", (("May","5"),("May","6"),("June","7"))) == True

def test_case019():
    # day appears in two different months — not unique
    assert unique_day("5", (("May","5"),("June","5"))) == False

def test_case020():
    # month with multiple entries where shared day makes it non-unique
    assert contains_unique_day("February", (("January","10"),("February","1"),("February","2"),("February","10"))) == True
