def top_k(lst, k):
    count = 0
    op = []
    while count < k:
        max_value = max(lst)
        op.append(max_value)
        lst.remove(max_value)
        count += 1
    return op