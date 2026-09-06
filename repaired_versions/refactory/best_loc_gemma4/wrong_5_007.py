def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    lst1 = list(lst)
    sorted_list = []
    
    # We need to find the biggest element k times
    # or until the list is empty
    count = 0
    while lst1 and count < k:
        # Initialize biggest with the first element of the current list
        biggest = lst1[0]
        for element in lst1:
            if element > biggest:
                biggest = element
        
        # Remove only one instance of the biggest element
        lst1.remove(biggest)
        sorted_list.append(biggest)
        count += 1
        
    return sorted_list