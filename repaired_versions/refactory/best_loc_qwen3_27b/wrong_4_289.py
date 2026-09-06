def sort_age(lst):
    new_list = []
    while lst:
        largest = -1
        largest_person = None
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                largest_person = i
        new_list.append(largest_person)
        lst.remove(largest_person)
    return new_list