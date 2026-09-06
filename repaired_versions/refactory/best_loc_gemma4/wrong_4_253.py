def sort_age(lst):
    list1 = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        biggest = temp_lst[0]
       
        for i in temp_lst:
            if i[1] > biggest[1]:
                biggest = i
                
        temp_lst.remove(biggest)
        list1.append(biggest)
    return list1