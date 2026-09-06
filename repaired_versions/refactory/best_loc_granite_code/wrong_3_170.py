def remove_extras(lst):
    a = []
    for element in lst:
        if element not in a:
            a.append(element)
    return a