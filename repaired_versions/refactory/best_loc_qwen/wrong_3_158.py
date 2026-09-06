def remove_extras(lst):
    new_lst = lst.copy()
    seen = set()
    result = []
    for i in new_lst:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result