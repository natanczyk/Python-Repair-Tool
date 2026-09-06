def top_k(lst, k):
    # Handle the case where k is 0 immediately to avoid entering the loop
    if k <= 0:
        return []
    
    # Create a copy of the list to avoid mutating the original input list
    temp_lst = list(lst)
    sort = []
    
    while temp_lst: 
        biggest = temp_lst[0]
        for element in temp_lst:
            if element > biggest:
                biggest = element
                
        temp_lst.remove(biggest)
        sort.append(biggest)
        if len(sort) == k:
            break
            
    return sort