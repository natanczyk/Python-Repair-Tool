def sort_age(lst):
    """selection sort"""
    l = len(lst)
    for i in range(l):
        largest_index = i
        for j in range(i+1, l):
            if lst[j][1] > lst[largest_index][1]:
                largest_index = j
        lst[i], lst[largest_index] = lst[largest_index], lst[i]
    return lst