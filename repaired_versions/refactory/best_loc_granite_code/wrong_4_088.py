def sort_age(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = [x for x in lst[1:] if x[1] > pivot[1]]
    right = [x for x in lst[1:] if x[1] <= pivot[1]]
    return sort_age(left) + [pivot] + sort_age(right)