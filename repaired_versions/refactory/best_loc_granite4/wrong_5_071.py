def top_k(lst, k):
    new = []
    for _ in range(k):
        if not lst:  # If the list is empty, break early
            break
        top = max(lst)
        lst.remove(top)
        new.append(top)
    return new