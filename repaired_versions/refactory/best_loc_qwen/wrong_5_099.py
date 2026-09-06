def top_k(lst, k):
    l = []
    if k <= 0:
        return []
    elif k == 1:
        return [max(lst)]
    else:
        a = max(lst)
        lst.remove(a)
        l.append(a)
        result = top_k(lst, k-1)
        l.extend(result)
        return l