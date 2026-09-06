def remove_extras(lst):
    seen = set()
    new_lst = []
    for elem in lst:
        if elem not in seen:
            seen.add(elem)
            new_lst.append(elem)
    return new_lst