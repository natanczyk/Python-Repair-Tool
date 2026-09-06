def top_k(lst, k):
    if lst == []:
        return []
    
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    sorted_lst = []
    
    while temp_lst:
        largest = temp_lst[0]
        for i in temp_lst:
            if i > largest:
                largest = i
        temp_lst.remove(largest)
        sorted_lst.append(largest)
        
    return sorted_lst[:k]