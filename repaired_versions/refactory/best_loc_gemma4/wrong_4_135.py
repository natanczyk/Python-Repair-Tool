def sort_age(lst):
    if not lst:
        return []
    
    # Find the person with the maximum age
    max_person = lst[0]
    for i in range(1, len(lst)):
        if lst[i][1] > max_person[1]:
            max_person = lst[i]
    
    # Create a copy of the list to avoid mutating the original input
    # and remove the person with the maximum age
    remaining = list(lst)
    remaining.remove(max_person)
    
    # Return the max person followed by the sorted remaining list
    return [max_person] + sort_age(remaining)