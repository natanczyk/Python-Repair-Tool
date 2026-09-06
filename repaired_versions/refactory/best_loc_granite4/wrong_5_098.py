def top_k(lst, k):
    if k <= 0 or not lst:
        return []
    if k == 1:
        return [max(lst)]
    a = max(lst)
    lst.remove(a)
    return [a] + top_k(lst, k - 1)