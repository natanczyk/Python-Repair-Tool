def top_k(lst, k):
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    new = []
    # We need to extract the maximum value k times
    for _ in range(k):
        if not temp_lst:
            break
        top = max(temp_lst) 
        new.append(top)
        temp_lst.remove(top)
        
    return new