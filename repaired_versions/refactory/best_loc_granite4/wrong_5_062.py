def top_k(lst, k):
    a = []
    while lst and len(a) < k:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        a.append(biggest)
    return a