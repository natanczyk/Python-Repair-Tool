def sort_age(lst):
    a = []
    for i in lst:
        a.append(i[1])
    
    sort = []
    temp_a = list(a)
    while temp_a:
        largest = temp_a[0]
        for element in temp_a:
            if element > largest:
                largest = element
        temp_a.remove(largest)
        sort.append(largest)
    
    lst2 = []
    for i in sort:
        for j in lst:
            if j[1] == i:
                lst2.append(j)
                break
    return lst2