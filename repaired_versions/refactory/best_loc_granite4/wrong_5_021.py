def top_k(lst, k):
    r = []
    for _ in range(k):
        biggest = lst[0]
        for num in lst:
            if biggest < num:
                biggest = num
        r.append(biggest)
        lst.remove(biggest)
    return r