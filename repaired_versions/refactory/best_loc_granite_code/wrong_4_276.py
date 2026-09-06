def sort_age(lst):
    sort=[]
    while lst:
        largest=lst[0][1]
        largest_person = lst[0]
        for i in lst:
            if i[1]>largest:
                largest=i[1]
                largest_person = i
        lst.remove(largest_person)
        sort.append(largest_person)
    return sort