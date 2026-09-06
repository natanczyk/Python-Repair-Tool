def sort_age(lst):
    sort = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        # Initialize the biggest person as the first person in the current list
        biggest_person = temp_lst[0]
        for person in temp_lst:
            if person[1] > biggest_person[1]:
                biggest_person = person
        # Remove the person with the maximum age and add them to the sorted list
        temp_lst.remove(biggest_person)
        sort.append(biggest_person)
    return sort