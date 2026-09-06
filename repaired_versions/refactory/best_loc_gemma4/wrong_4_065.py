def sort_age(lst):
    rslt=[]
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        largest = temp_lst[0]
        for element in temp_lst:
            if element[1] > largest[1]:
                largest = element
        temp_lst.remove(largest)
        rslt.append(largest)
    return rslt