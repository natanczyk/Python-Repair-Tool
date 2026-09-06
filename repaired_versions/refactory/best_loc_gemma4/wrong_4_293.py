def sort_age(lst):
    sort = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        biggest_person = None
        biggest_age = -1
        for person in temp_lst:
            if person[1] > biggest_age:
                biggest_age = person[1]
                biggest_person = person
        temp_lst.remove(biggest_person)
        sort.append(biggest_person)
    return sort