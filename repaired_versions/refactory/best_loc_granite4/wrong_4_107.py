def sort_age(lst):
    if not lst:
        return []
    sort = []
    while lst:
        largest = lst[0]
        for k in lst:
            if k[1] > largest[1]:
                largest = k
        lst.remove(largest)
        sort.append(largest)
    return sort