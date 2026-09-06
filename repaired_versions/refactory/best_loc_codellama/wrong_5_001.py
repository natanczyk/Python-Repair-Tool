def top_k(lst, k):
    result = []
    for i in range(k):
        big = max(lst)
        result.append(big)
        lst.remove(big)
    return result