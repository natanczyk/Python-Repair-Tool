def sort_age(lst):
    sorted_lst = []
    while lst:
        oldest = lst[0]
        for element in lst:
            if element[1] > oldest[1]:
                oldest = element
        lst.remove(oldest)
        sorted_lst.append(oldest)
    return sorted_lst