def sort_age(lst):
    new = []
    while lst:
        largest = lst[0][1]
        for i in lst:
            if i[1]>largest:
                largest = i[1]
        for j in lst[:]:
            if j[1] == largest:
                new.append(j)
                lst.remove(j)
    return new