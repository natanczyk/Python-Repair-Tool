def sort_age(lst):
    sort1 = []
    while lst:
        largest = lst[0][1]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
        for i in lst:
            if i[1] == largest:
                sort1.append(i)
                lst.remove(i)
                break
    return sort1