def remove_extras(lst):
    new_lst = []
    for i in range(len(lst)):
        if lst[i] not in lst[:i]:
            new_lst.append(lst[i])
    return new_lst