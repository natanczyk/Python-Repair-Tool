def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original
    remaining = lst[:]
    new_list = []
    
    for _ in range(k):
        if not remaining:
            break
        max_val = max(remaining)
        new_list.append(max_val)
        # Remove only one occurrence of max_val
        remaining.remove(max_val)
    
    return new_list