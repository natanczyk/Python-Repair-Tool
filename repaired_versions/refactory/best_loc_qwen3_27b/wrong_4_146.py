def sort_age(lst):
    if not lst:
        return []
    
    # Create a copy to avoid modifying the original list
    remaining = lst[:]
    sorted_list = []
    
    while remaining:
        # Find the person with the maximum age
        oldest_person = remaining[0]
        for elem in remaining:
            if elem[1] > oldest_person[1]:
                oldest_person = elem
        sorted_list.append(oldest_person)
        remaining.remove(oldest_person)
    
    return sorted_list