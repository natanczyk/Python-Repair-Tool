def remove_extras(lst):
    new_lst = []
    for k in range(len(lst)):
        if lst[k] not in new_lst:
            new_lst.append(lst[k])
    return new_lst