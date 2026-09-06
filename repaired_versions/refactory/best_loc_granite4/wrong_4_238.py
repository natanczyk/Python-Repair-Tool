def sort_age(lst):
    sorted_list = []
    while lst:
        oldest = lst[0]
        for x in lst:
            if x[1] > oldest[1]:
                oldest = x
        lst.remove(oldest)
        sorted_list.append(oldest)
    return sorted_list