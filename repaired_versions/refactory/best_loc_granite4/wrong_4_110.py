def sort_age(lst):
    new = []
    while lst:
        largest = lst[0][1]
        max_tuple = lst[0]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                max_tuple = i
        lst.remove(max_tuple)
        new.append(max_tuple)
    return new