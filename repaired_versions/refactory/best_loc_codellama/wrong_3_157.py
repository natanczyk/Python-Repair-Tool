def remove_extras(lst):
    seen = set()
    unique_lst = []
    for element in lst:
        if element not in seen:
            unique_lst.append(element)
            seen.add(element)
    return unique_lst