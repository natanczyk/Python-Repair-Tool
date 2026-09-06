def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original
    remaining = lst[:]
    op = []
    
    for _ in range(k):
        # Find the maximum value in the remaining list
        max_val = max(remaining)
        op.append(max_val)
        # Remove one occurrence of the max value from remaining
        remaining.remove(max_val)
    
    return op