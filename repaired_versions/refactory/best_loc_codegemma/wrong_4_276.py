def sort_age(lst):
    sort=[]
    while lst:
        largest=lst[0][1]
        for i in lst:
            if i[1]>largest:
                largest=i[1]
        for i in lst:
            if i[1]==largest:
                sort.append(i)
                lst.remove(i)
    return sort