def remove_extras(lst):
    new_list = []
    for i in range(len(lst)):
        if lst[i] not in new_list:
            new_list.append(lst[i])
    return new_list