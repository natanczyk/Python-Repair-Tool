def sort_age(lst):
    a=lst
    sort=[]
    while a:
        largest=a[0]
        for element in a:
            if element[1]>largest[1]:
                largest=element
        a.remove(largest)
        sort.append(largest)
    return sort