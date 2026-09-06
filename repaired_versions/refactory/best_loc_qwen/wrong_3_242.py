def remove_extras(lst):
    new_list = [lst[0]] if lst else []  # Handle empty list case
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list