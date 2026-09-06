def remove_extras(lst):
    seen = set()
    new_lst = []
    for elem in lst:
        if elem not in seen:
            new_lst.append(elem)
            seen.add(elem)
    return new_lst