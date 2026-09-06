def sort_age(lst):
    sort=[]
    while lst:
        biggest=lst[0][1]
        biggest_person = lst[0]
        for i in lst:
            if i[1]>biggest:
                biggest=i[1]
                biggest_person = i
        lst.remove(biggest_person)
        sort.append(biggest_person)
    return sort