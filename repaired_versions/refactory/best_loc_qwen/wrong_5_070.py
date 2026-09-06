def top_k(lst, k):
    new = []
    while len(new) < k:
        max_val = max(lst)
        new.append(max_val)
        lst.remove(max_val)
        
    return sorted(new, reverse=True)