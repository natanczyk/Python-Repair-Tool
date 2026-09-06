def top_k(lst, k):
    new = []
    while len(new) < k and lst:  # Ensure we only run while we need more elements and lst is not empty
        top = max(lst)
        new.append(top)
        lst.remove(top)
        
    return new