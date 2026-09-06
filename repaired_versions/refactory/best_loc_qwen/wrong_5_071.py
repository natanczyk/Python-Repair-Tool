def top_k(lst, k):
    new = []
    while k > 0:
        top = max(lst)
        new.append(top)
        lst.remove(top)
        k -= 1
        
    return sorted(new, reverse=True)