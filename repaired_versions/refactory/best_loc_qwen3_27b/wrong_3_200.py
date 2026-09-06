def remove_extras(lst):
    if lst == []:
        return []
    new_lst = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
    return new_lst