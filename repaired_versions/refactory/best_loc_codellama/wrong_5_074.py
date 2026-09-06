def top_k(lst, k):
    results = []
    while len(lst) > 0 and k > 0:
        max_value = max(lst)
        results.append(max_value)
        lst.remove(max_value)
        k -= 1
    return results