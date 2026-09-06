def sort_age(lst):
    sorted_list = []
    while lst:
        biggest = lst[0][1]
        max_tuple = lst[0]
        for i in lst:
            if i[1] > biggest:
                biggest = i[1]
                max_tuple = i
        lst.remove(max_tuple)
        sorted_list.append(max_tuple)
    return sorted_list