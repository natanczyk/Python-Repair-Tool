def sort_age(lst):
    if not lst:
        return []
    max_tuple = max(lst, key=lambda x: x[1])
    return [max_tuple] + sort_age([t for t in lst if t != max_tuple])