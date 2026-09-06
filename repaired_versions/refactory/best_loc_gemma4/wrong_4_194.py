def sort_age(lst):
    if not lst:
        return []
    
    # Find the person with the maximum age
    biggest_person = lst[0]
    for i in range(1, len(lst)):
        if lst[i][1] > biggest_person[1]:
            biggest_person = lst[i]
            
    # Create a new list excluding the biggest_person to avoid modifying the original list
    # and to handle the recursion correctly.
    remaining = list(lst)
    remaining.remove(biggest_person)
    
    return [biggest_person] + sort_age(remaining)