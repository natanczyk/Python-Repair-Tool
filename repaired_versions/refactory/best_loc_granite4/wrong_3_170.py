def remove_extras(lst):
    a = []
    for elem in lst:
        if elem not in a:
            a.append(elem)
    return a