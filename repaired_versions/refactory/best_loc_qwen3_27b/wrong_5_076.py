def top_k(lst, k):
    new = []
    # Make a copy to avoid modifying the original list if needed, 
    # but since we are removing from lst, let's work on a copy or just use the logic correctly
    # The bug is in the while condition: len(lst) > len(lst) - k is always true for k > 0
    # We want to extract the top k elements
    working_lst = lst[:]
    while len(new) < k:
        top = max(working_lst) 
        new.append(top)
        working_lst.remove(top)
        
    return new