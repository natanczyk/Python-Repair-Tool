def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original
    lst_copy = lst[:]
    result = []
    
    # Find the top k elements
    for _ in range(k):
        if not lst_copy:  # If the list is empty, break early
            break
        # Find the maximum value in the remaining list
        max_val = lst_copy[0]
        for num in lst_copy:
            if num > max_val:
                max_val = num
        result.append(max_val)
        # Remove the found maximum from the copy
        lst_copy.remove(max_val)
    
    return result