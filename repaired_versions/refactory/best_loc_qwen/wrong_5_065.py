def top_k(lst, k):
    x = []
    for _ in range(k):
        max_val = float('-inf')
        for j in lst:
            if j > max_val:
                max_val = j
        x.append(max_val)
        lst.remove(max_val)
    return sorted(x, reverse=True)