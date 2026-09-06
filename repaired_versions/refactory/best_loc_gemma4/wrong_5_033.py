def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    final = []
    
    # We need to find the largest element k times
    while len(final) < k and temp_lst:
        largest = temp_lst[0]
        # Find the maximum value in the current list
        for element in temp_lst:
            if element > largest:
                largest = element
        
        # Append the found maximum to the result list
        final.append(largest)
        # Remove only one instance of the maximum value from the list
        temp_lst.remove(largest)
        
    return final