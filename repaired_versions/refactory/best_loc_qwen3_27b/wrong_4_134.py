def sort_age(lst):
    if lst == []:
        return []
    
    # Find the tuple with the maximum age
    max_tuple = lst[0]
    for i in range(1, len(lst)):
        if lst[i][1] > max_tuple[1]:
            max_tuple = lst[i]
    
    # Create a new list with the max tuple at the front
    new_lst = [max_tuple]
    
    # Remove the max tuple from the original list
    lst.remove(max_tuple)
    
    # Recursively sort the remaining list and append
    new_lst.extend(sort_age(lst))
    
    return new_lst