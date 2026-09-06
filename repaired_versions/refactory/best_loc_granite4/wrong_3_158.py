def remove_extras(lst):
    new_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            new_lst.append(item)
            seen.add(item)
    return new_lst