def top_k(lst, k):
    sort = []
    while lst:
        biggest = lst[0]
        for i in lst[1:]:
            if i > biggest:
                biggest = i
        lst.remove(biggest)
        sort.append(biggest)
    
    if k > len(sort):
        k = len(sort)
    return sort[:k]  # Take the first k elements which are already in descending order