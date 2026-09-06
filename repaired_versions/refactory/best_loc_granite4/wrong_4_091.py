def sort_age(lst):
    if not lst:
        return []
    # Find the tuple with the maximum age
    holder = max(lst, key=lambda x: x[1])
    # Recursively sort the remaining list after removing the holder
    return [holder] + sort_age([x for x in lst if x != holder])