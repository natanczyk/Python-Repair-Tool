def sort_age(lst):
    new_list = []
    while lst:
        largest = 0
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                largest_index = lst.index(i)
        new_list.append(lst.pop(largest_index))
    return new_list