def sort_age(lst):
    a = []
    for i in lst:
        a.append(i[1])
    print(a)
    sort = []
    while a:
        largest = a[0]
        for element in a:
            if element > largest:
                largest = element
        a.remove(largest)
        sort.append(largest)
    print(sort)
    lst2 = []
    for i in sort:
        for j in lst:
            if j[1] == i:
                lst2.append(j)
    return lst2