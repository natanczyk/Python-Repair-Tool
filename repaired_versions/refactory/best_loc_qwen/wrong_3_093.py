def remove_extras(lst):
    sub_list = []
    seen = set()
    for elem in lst:
        if elem not in seen:
            sub_list.append(elem)
            seen.add(elem)
    return sub_list