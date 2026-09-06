def remove_extras(lst):
    seen = set()
    unique_list = []
    for elem in lst:
        if elem not in seen:
            unique_list.append(elem)
            seen.add(elem)
    return unique_list