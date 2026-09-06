def remove_extras(lst):
    occurrences = set()
    new_list = []
    for item in lst:
        if item not in occurrences:
            occurrences.add(item)
            new_list.append(item)
    return new_list