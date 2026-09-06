def sort_age(lst):
    sort=[]
    while lst:
        largest=lst[0][1]
        largest_item = lst[0]
        for i in lst:
            if i[1]>largest:
                largest=i[1]
                largest_item = i
        lst.remove(largest_item)
        sort.append(largest_item)
    return sort