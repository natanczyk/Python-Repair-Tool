def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    new = []
    for i in range(k):
        # Find the index of the maximum element
        max_val = temp_lst[0]
        max_idx = 0
        for idx in range(1, len(temp_lst)):
            if temp_lst[idx] > max_val:
                max_val = temp_lst[idx]
                max_idx = idx
        
        # Append the maximum value to the result and remove it from the temporary list
        new.append(temp_lst.pop(max_idx))
        
    return new