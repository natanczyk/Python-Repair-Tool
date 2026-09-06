def remove_extras(lst):
    new_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            new_lst.append(item)
    return new_lst