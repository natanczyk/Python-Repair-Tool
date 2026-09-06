def sort_age(lst):
    sorted_lst = []
    while lst:
        oldest = lst[0]
        for elem in lst:
            if elem[1] > oldest[1]:
                oldest = elem
        lst.remove(oldest)
        sorted_lst.append(oldest)
    return sorted_lst