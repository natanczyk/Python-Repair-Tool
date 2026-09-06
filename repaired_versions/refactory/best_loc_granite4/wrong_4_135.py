def sort_age(lst):
    if not lst:
        return []
    max_index = 0
    for i in range(1, len(lst)):
        if lst[i][1] > lst[max_index][1]:
            max_index = i
    return [lst[max_index]] + sort_age([x for i, x in enumerate(lst) if i != max_index])