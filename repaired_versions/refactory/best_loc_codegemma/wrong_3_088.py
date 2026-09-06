def remove_extras(lst):
    sub_list = []
    for elem in lst:
        if elem not in sub_list:
            sub_list.append(elem)
    return sub_list