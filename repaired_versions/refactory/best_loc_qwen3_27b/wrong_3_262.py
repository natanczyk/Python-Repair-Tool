def remove_extras(lst):
    seen = []
    for element in lst:
        if element not in seen:
            seen.append(element)
    return seen