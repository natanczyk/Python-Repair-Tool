def sort_age(lst):
    new = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        eldest = temp_lst[0]
        for i in temp_lst:
            # Compare based on the age (the second element of the tuple)
            if i[1] > eldest[1]:
                eldest = i 
        temp_lst.remove(eldest)
        new.append(eldest)
    return new