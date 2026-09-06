def remove_extras(lst):
    new_list = []
    for element in lst:
        if element not in new_list:
            new_list.append(element)
    return new_list