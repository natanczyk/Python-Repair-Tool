def sort_age(lst):
    if lst == []:
        return []
    
    # Find the person with the maximum age
    max_person = lst[0]
    for x in lst[1:]:
        if x[1] > max_person[1]:
            max_person = x
    
    # Create a new list without the max_person
    remaining = [x for x in lst if x != max_person]
    
    # Return the max_person as a single-element list concatenated with the sorted remaining list
    return [max_person] + sort_age(remaining)