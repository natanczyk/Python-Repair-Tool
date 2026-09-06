def top_k(lst, k):
    count = 0
    op = []
    while count < k:
        max_val = max(lst)
        op.append(max_val)
        lst.remove(max_val)
        count += 1
    return sorted(op, reverse=True)