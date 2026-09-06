def sort_age(lst):
    sort = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        # Start by assuming the first element is the oldest
        oldest = temp_lst[0]
        for element in temp_lst:
            # Compare ages (index 1 of the tuple) to find the maximum
            if element[1] > oldest[1]:
                oldest = element
        
        # Remove the oldest person from the temporary list and add to the sorted list
        temp_lst.remove(oldest)
        sort.append(oldest)
        
    return sort