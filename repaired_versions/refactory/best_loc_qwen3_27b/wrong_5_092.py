def top_k(lst, k):
    if k == 0:
        return []
    
    # Create a copy to avoid modifying the original list
    lst_copy = lst[:]
    
    # Implement selection sort-like approach to find top k elements
    result = []
    for _ in range(k):
        if not lst_copy:
            break
        # Find the maximum value in the remaining list
        max_val = lst_copy[0]
        max_idx = 0
        for i in range(1, len(lst_copy)):
            if lst_copy[i] > max_val:
                max_val = lst_copy[i]
                max_idx = i
        result.append(max_val)
        # Remove the found maximum from the list
        lst_copy.pop(max_idx)
    
    return result