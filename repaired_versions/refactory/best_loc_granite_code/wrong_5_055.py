def top_k(lst, k):
    values = []
    greatest = max(lst)
    while len(values) < k:
        values.append(greatest)
        lst.remove(greatest)
        if lst:
            greatest = max(lst)
    return values