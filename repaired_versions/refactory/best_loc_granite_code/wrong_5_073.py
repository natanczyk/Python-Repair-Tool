def top_k(lst, k):
    results = []
    counter = 0
    while counter < k:
        max_value = max(lst)
        max_index = lst.index(max_value)
        results.append(max_value)
        lst.pop(max_index)
        counter += 1
    return results