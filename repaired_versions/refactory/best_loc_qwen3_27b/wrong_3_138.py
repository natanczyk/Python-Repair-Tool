def remove_extras(lst):
    lst1 = []
    for i in range(len(lst)):
        if lst[i] not in lst1:
            lst1.append(lst[i])
    return lst1