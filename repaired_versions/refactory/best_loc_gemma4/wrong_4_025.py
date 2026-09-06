def sort_age(lst):
    sort = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst: 
        # Initialize biggest as the first element
        biggest = temp_lst[0]
        for element in temp_lst:
            # Compare based on the age (the second element of the tuple)
            if element[1] > biggest[1]:
                biggest = element
        # Remove the found biggest element from the temporary list
        temp_lst.remove(biggest)
        # Append it to the sorted list
        sort.append(biggest)
    return sort