def top_k(lst, k):
    # Implementing a simple selection sort to find the top k elements
    lst_copy = lst[:]  # Work on a copy to avoid modifying the original list
    result = []
    
    for _ in range(k):
        if not lst_copy:  # If the list is empty, break early
            break
        max_val = lst_copy[0]
        max_index = 0
        for index, value in enumerate(lst_copy):
            if value > max_val:
                max_val = value
                max_index = index
        result.append(max_val)
        lst_copy.pop(max_index)  # Remove the found max element from consideration
    
    return result