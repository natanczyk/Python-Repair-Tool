def top_k(lst, k):
    new = []
    for _ in range(k):
        new.append(max(lst))
        lst.remove(max(lst))
    return new