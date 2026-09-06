def sort_age(lst):
    if len(lst) == 0:
        return lst
    biggest = max(lst, key=lambda x: x[1])
    return [biggest] + sort_age([x for x in lst if x != biggest])