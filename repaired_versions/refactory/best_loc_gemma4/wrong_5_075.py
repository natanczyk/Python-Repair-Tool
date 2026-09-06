def top_k(lst, k):
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    new = []
    # Continue extracting the maximum element until we have k elements 
    # or the list is empty
    while len(new) < k and len(temp_lst) > 0:
        top = max(temp_lst) 
        new.append(top)
        temp_lst.remove(top)
        
    return new