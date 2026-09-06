def sort_age(lst):
    # Create a copy of the list to avoid mutating the original input
    a = list(lst)
    sort = []
    while a: 
        # Initialize biggest with the first element
        biggest = a[0]
        for element in a:
            # Compare based on the age (the second element of the tuple)
            if element[1] > biggest[1]:
                biggest = element
        # Remove the found biggest element from the temporary list
        a.remove(biggest)
        # Append it to the result list
        sort.append(biggest)
    return sort