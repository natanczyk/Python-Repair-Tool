def top_k(lst, k):
    op = []
    while len(op) < k:
        op.append(max(lst))
        lst.remove(max(lst))
    return op