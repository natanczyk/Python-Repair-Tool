def top_k(lst, k):
    if k > len(lst):
        return False
    elif k == 0:
        return []
    elif k == 1:
        return [max(lst)]
    else:
        a = max(lst)
        lst.remove(a)
        return [a] + top_k(lst, k - 1)