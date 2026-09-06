def sort_age(lst):
    sort=[]
    while lst:
        biggest=lst[0]
        for i in lst:
            if i[1]>biggest[1]:
                biggest=i
        sort.append(biggest)
        lst.remove(biggest)
    return sort