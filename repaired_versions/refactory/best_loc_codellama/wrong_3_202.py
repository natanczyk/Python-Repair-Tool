def remove_extras(lst):
    new_lst = []
    if not lst:
        return []
    for i in range(len(lst)):
        a = lst[i]
        if a not in new_lst:
            new_lst.append(a)
    return new_lst