def remove_extras(lst):
    seen = set()
    new_lst = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            new_lst.append(item)
    return new_lst