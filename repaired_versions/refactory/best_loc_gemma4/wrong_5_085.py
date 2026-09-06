def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    result = []
    
    # We need to find the k largest elements
    while len(result) < k and temp_lst:
        biggest = temp_lst[0]
        for element in temp_lst:
            if element > biggest:
                biggest = element
        result.append(biggest)
        # Remove only one instance of the biggest element
        temp_lst.remove(biggest)
        
    return result