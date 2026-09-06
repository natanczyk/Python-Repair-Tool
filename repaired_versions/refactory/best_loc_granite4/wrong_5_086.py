def top_k(lst, k):
    result = []
    while len(result) < k and lst:
        a = max(lst)
        lst.remove(a)
        result.append(a)
    return result