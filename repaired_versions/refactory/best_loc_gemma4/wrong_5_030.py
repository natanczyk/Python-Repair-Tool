def top_k(lst, k):
    # Handle the case where k is 0 immediately to avoid adding any elements
    if k <= 0:
        return []
        
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    sort, output = [], []
    
    while temp_lst:
        largest = temp_lst[0]
        for i in temp_lst:
            if i > largest:
                largest = i
        temp_lst.remove(largest)
        sort.append(largest)
        
    for j in sort:
        output.append(j)
        if len(output) == k:
            break
            
    return output