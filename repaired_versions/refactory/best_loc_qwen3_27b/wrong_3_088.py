def remove_extras(lst):
    seen = []
    for elem in lst:
        if elem not in seen:
            seen.append(elem)
    return seen