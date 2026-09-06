def remove_extras(lst):
    result = []
    seen = set()
    for elem in lst:
        if elem not in seen:
            result.append(elem)
            seen.add(elem)
    return result