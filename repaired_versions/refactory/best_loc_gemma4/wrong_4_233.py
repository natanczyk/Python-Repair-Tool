def sort_age(lst):
    sort = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        # Initialize largest as the first element of the current list
        largest = temp_lst[0]
        for element in temp_lst:
            # Compare the age (index 1 of the tuple)
            if element[1] > largest[1]:
                largest = element
        # Remove the found largest element from the temporary list
        temp_lst.remove(largest)
        # Append it to the sorted result list
        sort.append(largest)
    return sort