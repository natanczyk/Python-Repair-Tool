def top_k(lst, k):
    new = []
    while len(new) < k:
        max_val = max(lst)
        lst.remove(max_val)
        new.append(max_val)
        
    return sorted(new, reverse=True)