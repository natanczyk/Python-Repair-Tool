def sort_age(lst):
    sort = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst: 
        # Initialize biggest with the first element of the current list
        biggest = temp_lst[0]
        for element in temp_lst:
            # Compare based on the age (the second element of the tuple)
            if element[1] > biggest[1]:
                biggest = element
        temp_lst.remove(biggest)
        sort.append(biggest)
    return sort