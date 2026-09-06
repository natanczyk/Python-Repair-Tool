def sort_age(lst):
    sort=[]
    while lst:
        biggest=0
        biggest_person=None
        for i in lst:
            if i[1]>biggest:
                biggest=i[1]
                biggest_person=i
        lst.remove(biggest_person)
        sort.append(biggest_person)
    return sort