def top_k(lst, k):
    new = []
    while len(new) < k:
        max_val = max(lst)
        max_index = lst.index(max_val)
        new.append(max_val)
        lst.pop(max_index)
        
    return sorted(new, reverse=True)