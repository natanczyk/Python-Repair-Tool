def remove_extras(lst):
    result = []
    seen = set()
    for element in lst:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result