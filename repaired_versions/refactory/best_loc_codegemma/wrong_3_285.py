def remove_extras(lst):
    lst2 = []
    for x in lst:
        if lst.count(x) > 0 and x not in lst2:
            lst2.append(x)
    return lst2