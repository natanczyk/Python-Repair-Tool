def remove_extras(lst):
    seen = set()
    new_lst = []
    for element in lst:
        if element not in seen:
            new_lst.append(element)
            seen.add(element)
    return new_lst