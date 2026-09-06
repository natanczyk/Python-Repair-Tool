def remove_extras(lst):
    list1 = []
    for i in lst:
        if i not in list1:
            list1.append(i)
    return list1