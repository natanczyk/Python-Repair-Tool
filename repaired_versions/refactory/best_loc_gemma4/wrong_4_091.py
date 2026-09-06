def sort_age(lst):
    if not lst:
        return []
    
    # Find the person with the maximum age
    holder = lst[0]
    for x in lst:
        if x[1] > holder[1]:
            holder = x
            
    # Create a new list excluding the person with the maximum age
    # to avoid modifying the original list and to avoid NoneType errors
    remaining = [x for x in lst if x != holder]
    
    # Return the oldest person followed by the sorted remaining list
    return [holder] + sort_age(remaining)