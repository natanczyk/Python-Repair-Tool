def top_k(lst, k):
    result = []
    while lst and len(result) < k:
        a = max(lst)
        lst.remove(a)
        result.append(a)
    return result