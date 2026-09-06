def top_k(lst, k):
    sort = []
    while len(sort) < k and lst:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        sort.append(biggest)
    return sort