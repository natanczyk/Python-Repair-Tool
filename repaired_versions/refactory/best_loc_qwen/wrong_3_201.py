def remove_extras(lst):
    lst1 = []
    for item in lst:
        if item not in lst1:
            lst1.append(item)
    return lst1