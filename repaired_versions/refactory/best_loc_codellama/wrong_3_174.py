def remove_extras(lst):
    seen = set()
    new_lst = []
    for element in lst:
        if element not in seen:
            seen.add(element)
            new_lst.append(element)
    return new_lst