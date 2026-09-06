def top_k(lst, k):
    results = []
    for i in range(k):
        max_value = max(lst)
        results.append(max_value)
        lst.remove(max_value)
    return results