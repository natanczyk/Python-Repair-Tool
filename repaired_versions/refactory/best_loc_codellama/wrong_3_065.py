def remove_extras(lst):
    new_lst = []
    for e in lst:
        if e not in new_lst:
            new_lst.append(e)
    return new_lst