def remove_extras(lst):
    seen = set()
    unique = []
    for elem in lst:
        if elem not in seen:
            unique.append(elem)
            seen.add(elem)
    return unique