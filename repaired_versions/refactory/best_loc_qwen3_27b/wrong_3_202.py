def remove_extras(lst):
    if lst == []:
        return []
    new_lst = [lst[0]]
    for i in range(1, len(lst)):
        a = lst[i]
        if a not in new_lst:
            new_lst.append(a)
    return new_lst