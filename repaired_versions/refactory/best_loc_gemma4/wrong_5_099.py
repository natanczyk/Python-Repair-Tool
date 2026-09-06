def top_k(lst, k):
    if k == 0:
        return []
    if k > len(lst):
        return False
    
    # Create a copy of the list to avoid mutating the original input
    lst_copy = list(lst)
    l = []
    
    # We need to find the max k times
    for _ in range(k):
        a = max(lst_copy)
        l.append(a)
        lst_copy.remove(a)
        
    return l