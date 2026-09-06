def top_k(lst, k):
    result = []
    while len(result) < k:
        a = max(lst)
        lst.remove(a)
        result.append(a)
    return sorted(result, reverse=True)