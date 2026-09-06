def top_k(lst, k):
    result = []
    
    # Create a copy to avoid modifying the original list
    working_lst = lst[:]
    
    # Loop until we have found k largest elements or the list is empty
    while len(result) < k and len(working_lst) > 0:
        biggest = working_lst[0]
        for element in working_lst:
            if element > biggest:
                biggest = element
        result.append(biggest)
        # Remove the first occurrence of the biggest element
        working_lst.remove(biggest)
        
    return result