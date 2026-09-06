def sort_age(lst):
    new_lst = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        oldest = temp_lst[0]
        for i in range(len(temp_lst)):
            if temp_lst[i][1] > oldest[1]:
                oldest = temp_lst[i]
        temp_lst.remove(oldest)
        new_lst.append(oldest)
    return new_lst