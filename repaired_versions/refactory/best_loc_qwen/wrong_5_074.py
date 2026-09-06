def top_k(lst, k):
    results = []
    counter = 0
    while counter < k:
        max_val = max(lst)
        max_index = lst.index(max_val)
        results.append(max_val)
        lst.pop(max_index)
        counter += 1
    return sorted(results, reverse=True)