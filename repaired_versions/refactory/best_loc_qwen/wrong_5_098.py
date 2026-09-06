def top_k(lst, k):
    if k <= 0:
        return []
    elif k == 1:
        return [max(lst)]
    else:
        a = max(lst)
        lst.remove(a)
        result = top_k(lst, k-1)
        result.insert(0, a)
        return result