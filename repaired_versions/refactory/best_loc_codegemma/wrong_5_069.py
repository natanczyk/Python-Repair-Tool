def top_k(lst, k):
    new = []
    while len(new) < k:
        new.append(lst.pop(lst.index(max(lst))))
        
    return new