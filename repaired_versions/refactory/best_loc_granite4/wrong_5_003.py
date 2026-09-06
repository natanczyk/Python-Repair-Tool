def top_k(lst, k):
    tmp = []
    while len(lst) > 0 and len(tmp) < k:
        tmp.append(max(lst))
        lst.remove(max(lst))
    return tmp