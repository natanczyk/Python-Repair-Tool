def sort_age(lst):
    new = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        curr = temp_lst[0]
        for i in temp_lst:
            # We want the older people at the front, so we find the maximum age
            if i[1] > curr[1]:
                curr = i
        # Remove the identified maximum age person and add them to the new list
        temp_lst.remove(curr)
        new.append(curr)
        
    return new