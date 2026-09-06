def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    new_lst = []
    counter = 0
    # The loop should run exactly k times to get k elements
    while counter < k:
        # Handle cases where k might be larger than the list size
        if not temp_lst:
            break
            
        highest = temp_lst[0]
        for x in temp_lst: 
            if x > highest:
                highest = x
        
        new_lst.append(highest)
        # Remove only one instance of the highest value
        temp_lst.remove(highest)
        counter += 1
        
    return new_lst