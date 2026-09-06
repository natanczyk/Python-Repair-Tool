def remove_extras(lst):
    unique_elements = set()
    removed = []
    for element in lst:
        if element not in unique_elements:
            removed.append(element)
            unique_elements.add(element)
    return removed