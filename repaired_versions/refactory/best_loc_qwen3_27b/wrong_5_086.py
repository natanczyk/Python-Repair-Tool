def top_k(lst, k):
    result = []
    lst = lst.copy()  # Avoid modifying the original list
    while len(result) < k:
        a = max(lst)
        lst.remove(a)
        result.append(a)
    return result