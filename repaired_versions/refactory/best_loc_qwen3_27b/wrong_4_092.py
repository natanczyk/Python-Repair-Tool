def sort_age(lst):
    # Create a copy of the list to avoid modifying the original
    remaining = lst[:]
    answer = []
    
    while remaining:
        # Find the person with the maximum age in the remaining list
        biggest = remaining[0]
        for i in range(1, len(remaining)):
            if remaining[i][1] > biggest[1]:
                biggest = remaining[i]
        
        # Remove the biggest from remaining and add to answer
        remaining.remove(biggest)
        answer.append(biggest)
    
    return answer