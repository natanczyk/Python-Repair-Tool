def sort_age(lst):
    """selection sort"""
    l = len(lst)
    for i in range(l):
        # Track the index of the largest element found in the remaining list
        largest_idx = i
        for j in range(i + 1, l):
            if lst[j][1] > lst[largest_idx][1]:
                largest_idx = j
        
        # Swap the found maximum element with the element at the current position
        lst[i], lst[largest_idx] = lst[largest_idx], lst[i]
        
    return lst