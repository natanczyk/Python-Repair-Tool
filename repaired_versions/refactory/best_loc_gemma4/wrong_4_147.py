def sort_age(lst):
    sorted_list = []
    # Create a copy of the list to avoid mutating the original input list
    temp_lst = list(lst)
    while temp_lst:
        oldest = temp_lst[0]
        for elem in temp_lst:
            if elem[1] > oldest[1]:
                oldest = elem
        temp_lst.remove(oldest)
        sorted_list.append(oldest)
    return sorted_list