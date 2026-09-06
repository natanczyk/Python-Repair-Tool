def remove_extras(lst):
    seen = set()
    new_lst = []
    for x in lst:
        if x not in seen:
            new_lst.append(x)
            seen.add(x)
    return new_lst