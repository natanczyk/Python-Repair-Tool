def sort_age(lst):
    newlst = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        current = temp_lst[0]
        for element in temp_lst:
            # To sort in descending order (older people first), 
            # we search for the maximum age in each iteration.
            if element[1] > current[1]:
                current = element
        newlst.append(current)
        temp_lst.remove(current)
    return newlst