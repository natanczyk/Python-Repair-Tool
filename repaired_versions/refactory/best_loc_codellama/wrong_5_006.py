def top_k(lst, k):
    sort = []
    while lst: 
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        if len(sort) < k:
            sort.append(biggest)
        lst.remove(biggest)
    return sort