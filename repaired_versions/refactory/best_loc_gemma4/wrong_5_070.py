def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    new = []
    
    # We need to find the maximum element k times
    for _ in range(k):
        if not temp_lst:
            break
        # Find the maximum value in the current list
        max_val = max(temp_lst)
        # Append the value to our result list
        new.append(max_val)
        # Remove only one instance of that maximum value from the temporary list
        temp_lst.remove(max_val)
        
    return new