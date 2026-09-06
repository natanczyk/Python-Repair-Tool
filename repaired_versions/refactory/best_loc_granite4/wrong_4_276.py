def sort_age(lst):
    sort = []
    while lst:
        largest = lst[0][1]
        largest_tuple = lst[0]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                largest_tuple = i
        lst.remove(largest_tuple)
        sort.append(largest_tuple)
    return sort