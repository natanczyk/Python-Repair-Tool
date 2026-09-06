def remove_extras(lst):
    seen = set()
    unique = []
    for element in lst:
        if element not in seen:
            unique.append(element)
            seen.add(element)
    return unique