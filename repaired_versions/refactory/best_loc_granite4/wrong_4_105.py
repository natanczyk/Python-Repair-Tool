def sort_age(lst):
    sort1 = []
    while lst:
        largest = lst[0][1]
        max_tuple = lst[0]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                max_tuple = i
        lst.remove(max_tuple)
        sort1.append(max_tuple)
    return sort1