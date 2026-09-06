def sort_age(lst):
    """selection sort"""
    l = len(lst)
    for i in range(l):
        largest_idx = i
        for j in range(i+1, l):
            if lst[j][1] > lst[largest_idx][1]:
                largest_idx = j
        lst[i], lst[largest_idx] = lst[largest_idx], lst[i]
    return lst