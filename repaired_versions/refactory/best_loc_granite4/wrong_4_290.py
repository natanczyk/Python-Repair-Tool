def sort_age(lst):
    new_list = []
    while lst:
        largest = lst[0][1]
        count = lst[0]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                count = i
        new_list.append(count)
        lst.remove(count)
    return new_list