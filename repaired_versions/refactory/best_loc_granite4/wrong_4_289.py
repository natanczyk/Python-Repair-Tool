def sort_age(lst):
    new_list = []
    while lst:
        largest = lst[0][1]
        index = 0
        for i, person in enumerate(lst):
            if person[1] > largest:
                largest = person[1]
                index = i
        new_list.append(lst[index])
        lst.pop(index)
    return new_list