def top_k(lst, k):
    sotsot = []
    # Make a copy to avoid modifying the original list if needed, 
    # but since we are removing from lst, let's work with a copy
    working_lst = lst[:]
    
    # We need to find the top k elements
    for _ in range(k):
        if not working_lst:
            break
        max_val = max(working_lst)
        sotsot.append(max_val)
        working_lst.remove(max_val)
    
    return sotsot