def sort_age(lst):
    # Create a copy of the list to avoid modifying the original input
    old_lst = list(lst)
    new_lst = []
    while old_lst:
        # Initialize largest with the first element of the current list
        largest = old_lst[0]
        for i in old_lst:
            # Compare based on the age (the second element of the tuple)
            if i[1] > largest[1]:
                largest = i
        # Remove the found largest element from the working list
        old_lst.remove(largest)
        # Append it to the result list
        new_lst.append(largest)
    return new_lst