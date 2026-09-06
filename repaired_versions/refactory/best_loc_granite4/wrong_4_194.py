def sort_age(lst):
    if not lst:
        return []
    biggest = max(lst, key=lambda x: x[1])
    return [biggest] + sort_age([x for x in lst if x != biggest])