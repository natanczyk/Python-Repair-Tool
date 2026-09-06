def remove_extras(lst):
    if not lst:
        return []
    new_lst = [lst[0]]
    if len(lst) > 1:
        rest = remove_extras(lst[1:])
        for item in rest:
            if item not in new_lst:
                new_lst.append(item)
    return new_lst