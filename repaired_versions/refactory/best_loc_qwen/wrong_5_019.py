def top_k(lst, k):
    arranged = []
    while k > 0:
        max_val = max(lst)
        arranged.append(max_val)
        lst.remove(max_val)
        k -= 1
    return arranged