def sort_age(lst):
    if not lst:
        return []
    # Find the tuple with the maximum age
    max_tuple = max(lst, key=lambda x: x[1])
    # Recursively sort the remaining list
    return [max_tuple] + sort_age([x for x in lst if x != max_tuple])