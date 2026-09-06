def top_k(lst, k):
    new_list = []
    # Work on a copy of the list to avoid modifying the original
    remaining = lst[:]
    for _ in range(k):
        if not remaining:  # If the list is empty, break early
            break
        max_val = max(remaining)
        new_list.append(max_val)
        remaining.remove(max_val)
    return new_list