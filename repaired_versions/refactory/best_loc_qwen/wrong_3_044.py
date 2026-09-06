def remove_extras(lst):
    new_lst = []
    seen = set()
    for i in lst:
        if i not in seen:
            new_lst.append(i)
            seen.add(i)
    return new_lst