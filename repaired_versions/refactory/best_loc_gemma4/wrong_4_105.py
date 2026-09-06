def sort_age(lst):
    sort1 = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        # Initialize the person with the largest age as the first element
        largest_person = temp_lst[0]
        for person in temp_lst:
            if person[1] > largest_person[1]:
                largest_person = person
        # Remove the person with the largest age from the temporary list
        temp_lst.remove(largest_person)
        # Append that person to the sorted list
        sort1.append(largest_person)
    return sort1