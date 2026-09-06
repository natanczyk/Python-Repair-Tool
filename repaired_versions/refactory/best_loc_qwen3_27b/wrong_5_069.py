def top_k(lst, k):
    # Make a copy to avoid modifying the original list
    lst = lst[:]
    new = []
    while len(new) < k:
        # Find the index of the maximum value
        max_val = max(lst)
        max_idx = lst.index(max_val)
        new.append(lst.pop(max_idx))
        
    return new