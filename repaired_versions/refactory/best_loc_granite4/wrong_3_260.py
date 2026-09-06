def remove_extras(lst):
    seen = set()
    result = []
    for element in lst:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result