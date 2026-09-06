def sort_age(lst):
    if not lst:
        return []
    
    # Find the person with the maximum age
    max_person = lst[0]
    for person in lst[1:]:
        if person[1] > max_person[1]:
            max_person = person
    
    # Create a new list without the max_person
    remaining = [person for person in lst if person != max_person]
    
    # Recursively sort the remaining list and prepend the max_person
    return [max_person] + sort_age(remaining)