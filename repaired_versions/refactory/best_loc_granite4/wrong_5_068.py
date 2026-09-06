def top_k(lst, k):
    new = []
    for i in range(k):
        max_val = max(lst)
        new.append(max_val)
        lst.remove(max_val)
        
    return new