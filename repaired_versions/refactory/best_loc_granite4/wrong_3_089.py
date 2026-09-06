def remove_extras(lst):
    seen = set()
    result = []
    for elem in lst:
        if elem not in seen:
            seen.add(elem)
            result.append(elem)
    return result