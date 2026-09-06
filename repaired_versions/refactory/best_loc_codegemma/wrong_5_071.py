def top_k(lst, k):
    new = []
    while len(new) < k and lst:
        top = max(lst) 
        new.append(lst.pop(lst.index(top)))
        
    return new