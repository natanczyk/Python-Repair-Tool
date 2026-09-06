def top_k(lst, k):
    new = []
    for _ in range(k):
        if not lst:  # Handle case where k > len(lst)
            break
        max_val = max(lst)
        lst.remove(max_val)
        new.append(max_val)
    return new