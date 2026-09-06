def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    l = []
    if k > len(temp_lst):
        return False
    
    # Handle k=0 case explicitly or let the loop handle it
    if k == 0:
        return []
        
    # Extract the maximum element k times
    while len(l) < k:
        a = max(temp_lst)
        temp_lst.remove(a)
        l.append(a)
    
    return l