def sort_age(lst):
    result = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst != []:
        largest_tup = temp_lst[0]
        largest = temp_lst[0][1]
        for i in temp_lst:
            if i[1] > largest:
                largest_tup = i 
                largest = i[1]
        temp_lst.remove(largest_tup)
        result.append(largest_tup)
    return result