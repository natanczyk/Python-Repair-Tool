def top_k(lst, k):
    new = []
    # Create a copy of the list to avoid modifying the original
    lst = lst[:]
    for _ in range(k):
        if not lst:  # If the list is empty, break early
            break
        max_val = max(lst)
        new.append(max_val)
        lst.remove(max_val)  # Remove the first occurrence of the max value
    return new