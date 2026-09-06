def sort_age(lst):
    # Extract ages and sort them in descending order
    ages = [age for _, age in lst]
    ages.sort(reverse=True)
    
    # Build the sorted list of tuples based on the sorted ages
    sorted_lst = [person for age in ages for person in lst if person[1] == age]
    return sorted_lst