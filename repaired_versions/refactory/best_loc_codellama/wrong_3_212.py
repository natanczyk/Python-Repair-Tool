def remove_extras(lst):
    seen = set()
    result = []
    for elem in lst:
        if elem not in seen:
            result.append(elem)
            seen.add(elem)
    return result