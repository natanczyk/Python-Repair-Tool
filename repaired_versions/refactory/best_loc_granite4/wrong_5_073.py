def top_k(lst, k):
    results = []
    counter = 0
    while counter < k and lst:
        max_val = max(lst)
        results.append(max_val)
        lst.remove(max_val)
        counter += 1
    return results