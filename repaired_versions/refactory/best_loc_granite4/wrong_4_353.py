def sort_age(lst):
    # Fill in your code here
    # Extract ages and sort them in descending order
    sorted_ages = sorted((age for _, age in lst), reverse=True)
    
    # Build the result list using the sorted ages
    result = []
    for age in sorted_ages:
        for person in lst:
            if person[1] == age:
                result.append(person)
                break
    return result