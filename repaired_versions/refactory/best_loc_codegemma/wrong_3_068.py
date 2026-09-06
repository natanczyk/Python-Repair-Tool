def remove_extras(lst):
    unique_elements = []
    for i in lst:
        if i not in unique_elements:
            unique_elements.append(i)
    return unique_elements