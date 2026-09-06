def remove_extras(lst):
    occurrences = set()
    new_lst = []
    for item in lst:
        if item not in occurrences:
            occurrences.add(item)
            new_lst.append(item)
    return new_lst