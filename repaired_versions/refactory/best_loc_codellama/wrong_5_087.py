def top_k(lst, k):
    new = []
    while len(lst) > 0 and len(new) < k:
        a = max(lst)
        lst.remove(a)
        new.append(a)
    return new