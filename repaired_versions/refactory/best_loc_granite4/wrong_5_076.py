def top_k(lst, k):
    new = []
    while len(new) < k and lst:  # Ensure we stop when we have k elements or lst is empty
        top = max(lst)
        new.append(top)
        lst.remove(top)
        
    return new