def sort_age(lst):
    list1 = []
    # Create a copy of the list to avoid mutating the original input list
    temp_lst = list(lst)
    while temp_lst:
        # Assume the first element is the oldest
        biggest_tuple = temp_lst[0]
        for i in range(1, len(temp_lst)):
            # Compare the age (index 1 of the tuple)
            if temp_lst[i][1] > biggest_tuple[1]:
                biggest_tuple = temp_lst[i]
        
        # Remove the tuple object from the temporary list and add to result
        temp_lst.remove(biggest_tuple)
        list1.append(biggest_tuple)
    return list1