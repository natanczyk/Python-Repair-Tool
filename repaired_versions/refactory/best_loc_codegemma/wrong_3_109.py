def remove_extras(lst):
    seen = set()
    new_lst = []
    for k in lst:
        if k not in seen:
            new_lst.append(k)
            seen.add(k)
    return new_lst