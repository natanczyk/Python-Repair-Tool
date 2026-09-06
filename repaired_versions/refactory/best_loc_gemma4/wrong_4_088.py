def sort_age(lst):
    if not lst:
        return []
    
    # Find the person with the maximum age in the current list
    max_person = lst[0]
    for x in lst:
        if x[1] > max_person[1]:
            max_person = x
            
    # Create a new list excluding the max_person to avoid modifying the original list
    # and to handle the recursion correctly.
    remaining = [x for x in lst if x != max_person]
    
    # Return the max person in a list concatenated with the result of sorting the rest
    return [max_person] + sort_age(remaining)