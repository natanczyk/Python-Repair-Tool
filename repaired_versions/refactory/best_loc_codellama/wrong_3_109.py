def remove_extras(lst):
    seen = set()
    unique_elements = []
    for element in lst:
        if element not in seen:
            unique_elements.append(element)
            seen.add(element)
    return unique_elements