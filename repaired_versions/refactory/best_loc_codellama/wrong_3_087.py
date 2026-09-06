def remove_extras(lst):
    unique_elements = set()
    result = []
    for element in lst:
        if element not in unique_elements:
            result.append(element)
            unique_elements.add(element)
    return result