def sort_age(lst):
    if not lst:
        return []
    sorted_list = []
    while lst:
        max_age = lst[0][1]
        max_index = 0
        for i, person in enumerate(lst):
            if person[1] > max_age:
                max_age = person[1]
                max_index = i
        sorted_list.append(lst[max_index])
        lst.pop(max_index)
    return sorted_list