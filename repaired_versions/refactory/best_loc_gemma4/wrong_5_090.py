def top_k(lst, k):
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    sort = []
    
    # We only need the top k elements, so we can stop once we have k
    # or once the list is empty.
    while temp_lst and len(sort) < k:
        # Find the maximum value in the current list
        big = max(temp_lst)
        # Append it to our result list
        sort.append(big)
        # Remove only one instance of the maximum value
        temp_lst.remove(big)
    
    return sort