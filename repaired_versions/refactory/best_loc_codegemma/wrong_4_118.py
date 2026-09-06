def sort_age(lst):
    sort=[]
    if not lst:
        return []
    biggest=lst[0]
    for element in lst:
        if element[1] > biggest[1]:
            biggest=element
    sort.append(biggest)
    lst.remove(biggest)
    while lst:
        biggest=lst[0]
        for element in lst:
            if element[1] > biggest[1]:
                biggest=element
        sort.append(biggest)
        lst.remove(biggest)
    return sort