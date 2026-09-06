def sort_age(lst):
    if not lst:
        return []
    
    # Find the person with the maximum age
    holder = lst[0]
    for x in lst:
        if x[1] > holder[1]:
            holder = x
            
    # Create a new list excluding the person found (the maximum)
    # We use a list comprehension to remove only one instance of the max element
    remaining = []
    found = False
    for x in lst:
        if not found and x == holder:
            found = True
            continue
        remaining.append(x)
        
    return [holder] + sort_age(remaining)