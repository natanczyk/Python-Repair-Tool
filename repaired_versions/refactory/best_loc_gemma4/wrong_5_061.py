def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    new_lst = []
    
    # We only need to find the top k elements, not sort the whole list
    # This improves performance and ensures we meet the requirements
    for _ in range(k):
        if not temp_lst:
            break
        
        # Find the maximum element in the current list
        biggest = temp_lst[0]
        for x in temp_lst:
            if x > biggest:
                biggest = x
        
        # Remove the first occurrence of the maximum element
        temp_lst.remove(biggest)
        # Append it to our result list
        new_lst.append(biggest)
        
    return new_lst