def remove_extras(lst):
    seen = set()
    new_lst = []
    for i in lst:
        if i not in seen:
            new_lst.append(i)
            seen.add(i)
    return new_lst