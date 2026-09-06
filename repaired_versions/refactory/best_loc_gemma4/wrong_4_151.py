def sort_age(lst):
    new = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        # We want the older people at the front, so we find the maximum age
        max_age = temp_lst[0][1]
        gender = temp_lst[0][0]
        for ele in temp_lst:
            if ele[1] > max_age:
                max_age = ele[1]
                gender = ele[0]
        new.append((gender, max_age))
        temp_lst.remove((gender, max_age))
    return new