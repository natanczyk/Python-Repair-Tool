def remove_extras(lst):
    new_lst = []
    for a in lst:
        if a not in new_lst:
            new_lst.append(a)
    return new_lst