def sort_age(lst):
    if not lst:
        return []
    
    # Create a copy to avoid modifying the original list
    remaining = lst[:]
    sorted_list = []
    
    while remaining:
        # Find the element with the largest age
        largest = remaining[0]
        for element in remaining:
            if element[1] > largest[1]:
                largest = element
        remaining.remove(largest)
        sorted_list.append(largest)
    
    return sorted_list