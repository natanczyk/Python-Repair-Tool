def sort_age(lst):
    newlst = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        i = temp_lst[0]
        for element in temp_lst:
            if element[1] >= i[1]:
                i = element
        temp_lst.remove(i)
        newlst.append(i)
    return newlst