def top_k(lst, k):
    result = []
    while len(lst) > 0 and len(result) < k:
        a = max(lst)
        lst.remove(a)
        result.append(a)
    result.sort(reverse=True)
    return result