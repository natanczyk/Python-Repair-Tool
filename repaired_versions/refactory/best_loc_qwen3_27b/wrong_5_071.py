def top_k(lst, k):
    new = []
    # Work on a copy to avoid modifying the original list
    working_lst = lst[:]
    
    # We need to find the top k elements
    for _ in range(k):
        if not working_lst:
            break
        top = max(working_lst)
        new.append(top)
        working_lst.remove(top)
    
    return new