def sort_age(lst):
    sort_list = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        biggest = temp_lst[0]
        for element in temp_lst:
            if element[1] > biggest[1]:
                biggest = element
        temp_lst.remove(biggest)
        sort_list.append(biggest)
    return sort_list