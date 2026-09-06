def remove_extras(lst):
    seen = set()
    result = []
    for element in lst:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result