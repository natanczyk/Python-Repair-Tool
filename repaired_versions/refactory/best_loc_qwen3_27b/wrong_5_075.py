def top_k(lst, k):
    new = []
    # Make a copy to avoid modifying the original list if needed, 
    # but since we are removing from lst, let's work on a copy or handle carefully.
    # The original code modifies lst directly. Let's create a working copy.
    working_lst = list(lst)
    
    while len(new) < k and len(working_lst) > 0:
        top = max(working_lst) 
        new.append(top)
        working_lst.remove(top)
        
    return new