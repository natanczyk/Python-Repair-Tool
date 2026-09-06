def remove_extras(lst):
    new_lst = []
    for i in range(0,len(lst)):
        a=lst[i]
        if a not in new_lst:
            new_lst.append(a)
    return new_lst