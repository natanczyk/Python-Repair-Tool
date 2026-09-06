def remove_extras(lst):
    a = []
    for item in lst:
        if item not in a:
            a += [item,]
    return a