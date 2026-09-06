def top_k(lst, k):
    # top k in descending order
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    result = []
    
    # We need to find the largest element k times
    for _ in range(k):
        if not temp_lst:
            break
            
        # Find the maximum element in the current list
        largest = temp_lst[0]
        for element in temp_lst:
            if element > largest:
                largest = element
        
        # Remove only one instance of the largest element and add to result
        temp_lst.remove(largest)
        result.append(largest)
        
    return result