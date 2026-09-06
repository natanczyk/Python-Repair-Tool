def sort_age(lst):
    sorted_list = []
    while lst:
        oldest = lst[0]
        oldest_index = 0
        for i in range(len(lst)):
            if lst[i][1] > oldest[1]:
                oldest = lst[i]
                oldest_index = i
        sorted_list.append(lst.pop(oldest_index))
    return sorted_list