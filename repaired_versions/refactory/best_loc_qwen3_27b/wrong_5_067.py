def top_k(lst, k):
    # Make a copy to avoid modifying the original list
    lst_copy = lst[:]
    new = []
    
    # We need to find the top k elements
    for _ in range(k):
        if not lst_copy:
            break
        # Find the maximum value in the remaining list
        max_val = max(lst_copy)
        # Remove the first occurrence of the max value
        lst_copy.remove(max_val)
        new.append(max_val)
    
    return new