def sort_age(lst):
    new_list=[]
    # We create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        largest = -1
        count = None
        for i in temp_lst:
            if i[1] > largest:
                largest = i[1]
                count = i
        new_list.append(count)
        temp_lst.remove(count)
    return new_list