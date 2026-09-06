def sort_age(lst):
    if not lst:
        return []
    
    # Find the person with the maximum age
    biggest = lst[0]
    for i in range(1, len(lst)):
        if lst[i][1] > biggest[1]:
            biggest = lst[i]
    
    # Create a new list without the biggest element
    remaining = [person for person in lst if person != biggest]
    
    return [biggest] + sort_age(remaining)