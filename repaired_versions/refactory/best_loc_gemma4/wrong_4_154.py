def sort_age(lst):
    new = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        small = temp_lst[0][1]
        name = temp_lst[0][0]
        for ele in temp_lst:
            if ele[1] > small:
                small = ele[1]
                name = ele[0]
        new.append((name, small))
        temp_lst.remove((name, small))
    return new