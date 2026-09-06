def sort_age(lst):
    if lst == []:
        return []
    
    # Find the person with the maximum age
    holder = lst[0]
    for x in lst[1:]:
        if x[1] > holder[1]:
            holder = x
    
    # Create a new list without the holder element
    remaining = [x for x in lst if x != holder]
    
    return [holder] + sort_age(remaining)