def sort_age(lst):
    """selection sort"""
    l = len(lst)
    for i in range(l):
        max_index = i
        for j in range(i + 1, l):
            if lst[j][1] > lst[max_index][1]:
                max_index = j
        lst[i], lst[max_index] = lst[max_index], lst[i]
    return lst