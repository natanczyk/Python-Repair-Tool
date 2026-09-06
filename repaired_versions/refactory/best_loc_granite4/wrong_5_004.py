def top_k(lst, k):
    sort = []
    while lst and len(sort) < k:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        sort.append(biggest)
    return sort