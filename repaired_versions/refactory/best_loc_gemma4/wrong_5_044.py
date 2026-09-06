def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    af_sort = []
    
    # We only need to find the top k elements, so we can stop once we have k
    while temp_lst and len(af_sort) < k:
        biggest = temp_lst[0] 
        for element in temp_lst:
            if element > biggest:
                biggest = element
        
        # Remove only one instance of the biggest element found
        temp_lst.remove(biggest)
        af_sort.append(biggest)
        
    return af_sort