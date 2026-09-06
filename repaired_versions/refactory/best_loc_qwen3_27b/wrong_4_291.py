def sort_age(lst):
    sort=[]
    while lst:
        biggest=lst[0][1]
        biggest_tuple = lst[0]
        for i in lst:
            if i[1]>biggest:
                biggest=i[1]
                biggest_tuple = i
        lst.remove(biggest_tuple)
        sort.append(biggest_tuple)
    return sort