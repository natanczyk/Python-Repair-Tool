def sort_age(lst):
    if lst == []:
        return []
    
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    sorted_lst = []
    
    while temp_lst:
        # Initialize largest as the first tuple in the current list
        largest = temp_lst[0]
        for i in temp_lst:
            # Compare based on the age (the second element of the tuple)
            if i[1] > largest[1]:
                largest = i
        
        # Remove the tuple with the maximum age and add it to the result list
        temp_lst.remove(largest)
        sorted_lst.append(largest)
        
    return sorted_lst