def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    sorted_list = []
    
    # Selection sort logic to find the maximum repeatedly
    while temp_lst:
        biggest = temp_lst[0]
        for i in temp_lst[1:]:
            if i > biggest:
                biggest = i
        
        # Remove the first occurrence of the biggest element found
        temp_lst.remove(biggest)
        sorted_list.append(biggest)
    
    # Return the first k elements of the sorted list
    return sorted_list[:k]