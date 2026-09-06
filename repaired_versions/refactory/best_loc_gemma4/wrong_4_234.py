def sort_age(lst):
    sorted_list = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        oldest = temp_lst[0]
        for element in temp_lst:
            if element[1] > oldest[1]:
                oldest = element
        temp_lst.remove(oldest)
        sorted_list.append(oldest)
    return sorted_list