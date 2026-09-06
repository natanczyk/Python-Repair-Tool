def sort_age(lst):
    new = []
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    while temp_lst:
        largest = temp_lst[0]
        for ele in temp_lst:
            if ele[1] > largest[1]:
                largest = ele
        temp_lst.remove(largest)
        new.append(largest)
    return new