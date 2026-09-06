def sort_age(lst):
    if not lst:
        return []
    
    # Create a copy to avoid modifying the original list
    remaining = lst[:]
    sorted_list = []
    
    while remaining:
        # Find the person with the largest age
        max_person = remaining[0]
        for person in remaining:
            if person[1] > max_person[1]:
                max_person = person
        
        # Remove the max person from remaining and add to sorted list
        remaining.remove(max_person)
        sorted_list.append(max_person)
    
    return sorted_list