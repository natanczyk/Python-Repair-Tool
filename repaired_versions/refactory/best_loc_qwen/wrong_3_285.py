def remove_extras(lst):
    lst2 = []
    for x in lst:
        if lst2.count(x) == 0:
            lst2.append(x)
    return lst2