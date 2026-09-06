def top_k(lst, k):
    # Make a copy to avoid modifying the original list
    lst_copy = lst[:]
    new = []
    for i in range(k):
        # Find the index of the maximum value
        max_val = max(lst_copy)
        max_idx = lst_copy.index(max_val)
        new.append(lst_copy.pop(max_idx))
        
    return new