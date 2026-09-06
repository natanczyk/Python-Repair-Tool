def sort_age(lst):
    list1 = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        biggest = temp_lst[0][1]
        b = temp_lst[0]
        for i in range(1, len(temp_lst)):
            if temp_lst[i][1] > biggest:
                biggest = temp_lst[i][1]
                b = temp_lst[i]
        temp_lst.remove(b)
        list1.append(b)
    return list1