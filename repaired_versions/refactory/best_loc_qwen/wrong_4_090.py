def sort_age(lst):
    holder = []
    if lst == []:
        return []
    for x in lst:
        if holder == [] or x[1] > holder[1]:
            holder = x
    return [holder] + sort_age([x for x in lst if x != holder])