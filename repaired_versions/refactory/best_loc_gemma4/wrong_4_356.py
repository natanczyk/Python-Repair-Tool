def sort_age(lst):
    # Fill in your code here
    newlst=[]
    # We create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        # Initialize maximum with the age of the first person in the current list
        max_person = temp_lst[0]
        for person in temp_lst:
            if person[1] > max_person[1]:
                max_person = person
        newlst.append(max_person)
        temp_lst.remove(max_person)

    return newlst