def remove_extras(lst):
    new_lst = [lst[0]] if lst else []
    if not lst:
        return []
    for i in range(len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
    return new_lst