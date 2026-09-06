def remove_extras(lst):
    new_list = []
    for e in lst:
        if not is_same(e, new_list):
            new_list.append(e)
    return new_list

def is_same(test, lst):
    for e in lst:
        if e == test:
            return True
    return False