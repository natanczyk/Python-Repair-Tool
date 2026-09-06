def sort_age(lst):
    if lst == []:
        return []
    holder = lst[0]
    for x in lst:
        if x[1] > holder[1]:
            holder = x
    return [holder] + sort_age([x for x in lst if x != holder])