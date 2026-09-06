def top_k(lst, k):
    #top k in descending order
    sort = []
    # Make a copy of the list to avoid modifying the original
    lst_copy = lst[:]
    
    # If k is 0, return empty list
    if k == 0:
        return sort
    
    # We need to find the top k elements
    for _ in range(k):
        if not lst_copy:
            break
        largest = lst_copy[0]
        for element in lst_copy:
            if element > largest:
                largest = element
        lst_copy.remove(largest)
        sort.append(largest)
    
    return sort