def sort_age(lst):
    if lst == []:
        return []
    
    # Find the tuple with the maximum age
    max_tuple = lst[0]
    for i in range(1, len(lst)):
        if lst[i][1] > max_tuple[1]:
            max_tuple = lst[i]
    
    # Create a new list without the max_tuple
    new_lst = [t for t in lst if t != max_tuple]
    
    # Return the max_tuple followed by the sorted rest
    return [max_tuple] + sort_age(new_lst)