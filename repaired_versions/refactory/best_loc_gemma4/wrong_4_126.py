def sort_age(lst):
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    sort = []
    while temp_lst:
        oldest = temp_lst[0]
        for i in temp_lst:
            if i[1] > oldest[1]:
                oldest = i
        temp_lst.remove(oldest)
        sort.append(oldest)
    return sort