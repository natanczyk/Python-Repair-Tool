def remove_extras(lst):
    if not lst:
        return []
    new_list = [lst[0]]
    for i in lst[1:]:
        if i not in new_list:
            new_list.append(i)
    return new_list