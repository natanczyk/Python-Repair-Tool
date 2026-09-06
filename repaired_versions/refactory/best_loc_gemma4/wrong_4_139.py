def sort_age(lst):
    # Create a copy of the list to avoid mutating the original input list
    temp_lst = list(lst)
    sort_list = []
    while temp_lst:
        # We want the older people at the front, so we find the maximum age
        largest = temp_lst[0]
        for element in temp_lst:
            if element[1] > largest[1]:
                largest = element
        temp_lst.remove(largest)
        sort_list.append(largest)
    return sort_list