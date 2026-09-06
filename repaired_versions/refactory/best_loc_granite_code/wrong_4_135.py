def sort_age(lst):
    if lst == []:
        return []
    small = max(lst, key=lambda x: x[1])
    return [small] + sort_age([x for x in lst if x != small])