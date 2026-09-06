def sort_age(lst):
    sorted_list = []
    while lst:
        oldest = lst[0]
        for elem in lst:
            if elem[1] > oldest[1]:
                oldest = elem
        lst.remove(oldest)
        sorted_list.append(oldest)
    return sorted_list