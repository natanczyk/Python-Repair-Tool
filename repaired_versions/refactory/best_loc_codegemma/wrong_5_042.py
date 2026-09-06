def top_k(lst, k):
    #top k in descending order
    sort = []
    x = len(lst)
    if x == 0:
        return []
    while len(sort) < k:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sort.append(largest)
    return sort