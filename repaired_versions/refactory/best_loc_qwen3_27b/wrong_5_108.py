def top_k(lst, k):
    # Handle edge cases
    if k <= 0 or not lst:
        return []
    
    # Make a copy to avoid modifying the original list
    lst = lst[:]
    
    new_lst = []
    counter = 0
    while counter < k:
        if not lst:
            break
        highest = lst[0]
        for x in lst:
            if x > highest:
                highest = x
        new_lst.append(highest)
        lst.remove(highest)
        counter += 1
        
    return new_lst