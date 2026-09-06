def sort_age(lst):
    if not lst:
        return []
    max_item = max(lst, key=lambda x: x[1])
    return [max_item] + sort_age([item for item in lst if item != max_item])