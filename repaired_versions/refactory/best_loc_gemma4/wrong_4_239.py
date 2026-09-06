def sort_age(lst):
    sort = []
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    while temp_lst:
        oldest = temp_lst[0]
        for x in temp_lst:
            if x[1] > oldest[1]:
                oldest = x
        temp_lst.remove(oldest)
        sort.append(oldest)
    return sort