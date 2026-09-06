def remove_extras(my_list):
    new_list = []
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
    return new_list