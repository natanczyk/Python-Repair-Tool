def remove_extras(lst):
    remove_lst = []
    seen = set()
    for i in lst:
        if i not in seen:
            remove_lst.append(i)
            seen.add(i)
    return remove_lst