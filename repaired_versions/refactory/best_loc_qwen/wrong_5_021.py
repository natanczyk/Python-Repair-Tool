def top_k(lst, k):
    r = []
    for _ in range(k):
        biggest = lst[0]
        for i in lst:
            if biggest < i:
                biggest = i
        r.append(biggest)
        lst.remove(biggest)
    return r