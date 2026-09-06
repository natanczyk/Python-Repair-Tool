def sort_age(lst):
    new = []
    while lst:
        largest = lst[0][1]
        largest_person = lst[0]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                largest_person = i
        lst.remove(largest_person)
        new.append(largest_person)
    return new