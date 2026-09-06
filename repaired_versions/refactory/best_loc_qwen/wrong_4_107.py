def sort_age(lst):
    sort = []
    while lst:
        largest = lst[0][1]
        largest_tuple = lst[0]
        for k in lst:
            if k[1] > largest:
                largest = k[1]
                largest_tuple = k
        lst.remove(largest_tuple)
        sort.append(largest_tuple)
    return sort