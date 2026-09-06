def top_k(lst, k):
    arranged = []
    while k > 0:
        max_val = max(lst)
        lst.remove(max_val)
        arranged.append(max_val)
        k = k-1
    return arranged