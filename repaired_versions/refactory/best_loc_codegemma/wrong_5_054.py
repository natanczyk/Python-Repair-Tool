def top_k(lst, k):
    count = 0
    op = []
    while count < k:
        big = max(lst)
        op += [big]
        lst.remove(big)
        count += 1
    return op