def top_k(lst, k):
    new = []
    # Work on a copy of the list to avoid modifying the original
    lst = lst[:]
    for _ in range(k):
        if not lst:  # If the list is empty, break early
            break
        max_val = max(lst)
        max_index = lst.index(max_val)
        new.append(lst.pop(max_index))
    return new