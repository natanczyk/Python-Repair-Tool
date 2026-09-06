def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original
    remaining = lst[:]
    result = []
    
    for _ in range(k):
        # Find the maximum value in the remaining list
        max_val = remaining[0]
        max_idx = 0
        for i in range(1, len(remaining)):
            if remaining[i] > max_val:
                max_val = remaining[i]
                max_idx = i
        # Add the max value to result
        result.append(max_val)
        # Remove the max value from remaining by index
        remaining.pop(max_idx)
    
    return result