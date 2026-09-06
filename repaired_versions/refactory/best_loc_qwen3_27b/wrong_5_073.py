def top_k(lst, k):
    # Make a copy to avoid modifying the original list
    lst_copy = lst[:]
    results = []
    
    # We need to find the top k elements
    for _ in range(k):
        if not lst_copy:
            break
        # Find the maximum value in the remaining list
        max_val = lst_copy[0]
        for val in lst_copy[1:]:
            if val > max_val:
                max_val = val
        # Remove the first occurrence of max_val from lst_copy
        lst_copy.remove(max_val)
        results.append(max_val)
    
    return results