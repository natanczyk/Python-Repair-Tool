def sort_age(lst):
    sort = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        oldest = temp_lst[0]
        for person in temp_lst:
            # Compare based on the age element (index 1) of the tuple
            if person[1] > oldest[1]:
                oldest = person
        temp_lst.remove(oldest)
        sort.append(oldest)
    return sort