def top_k(lst, k):
    op = []
    for _ in range(k):
        if not lst:  # Handle case where k > len(lst)
            break
        max_val = max(lst)
        op.append(max_val)
        lst.remove(max_val)
    return op